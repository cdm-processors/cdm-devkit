import * as vscode from 'vscode';

export class CdmMemoryWebviewPanel {
	memorySize!: number;
	offset!: number;
	length!: number;
	constructor(webviewPanel: vscode.WebviewPanel) {
	}
	getWebviewContent(content: string, offset: number, length: number){
		const memoryMapView = this.formatContent(content, offset, length);
		const header = this.getHeader();
		const setOffsetField = this.setInputFields(header);
		const htmlContent = `<html>
		<body>
			${setOffsetField}
			${memoryMapView}
		</body>
	</html>`;
		return htmlContent;
	}
	formatContent(content: string, offset: number, length: number){
		this.offset = offset;
		this.length = length;
		const splitContent: number[] =  content.split("\n").map(function (value){return Number(value);});
		const stackPointer = splitContent.pop();
		const memorySize = splitContent.length;
		this.memorySize = memorySize;
		const memoryMap: number[][] = [];
		const startLine = Math.floor(offset/16);
		length = Math.min(length, memorySize - startLine*16);
		for(let i = startLine; i<=startLine + Math.floor((length-1)/16); i++){
			memoryMap.push(splitContent.slice(i*16, (i+1)*16));
		}

		let memoryMapView = '';
		for(let i = 0; i <= Math.floor((length-1)/16); i++){
			memoryMapView += this.formatRow(memoryMap[i], stackPointer!, i+startLine, startLine, length);
		}
		
		
		memoryMapView = '<div>' + memoryMapView + '</div>';
		return memoryMapView;
	}
	formatRow(row: number[], stackPointer: number, numberOfRow: number, startLine: number, length: number){
		let formatedRow = '';
		let lastCell = 16;
		if (numberOfRow === startLine+Math.floor((length-1)/16) && length%16 !== 0){
			lastCell = length%16;
		}
		if (lastCell !== 0){
			formatedRow = `<pre><font size = "4"><font color="#a6a6a6">${numberOfRow.toString(16).padStart(3,'0') + '0 '}</font>`;
			for(let i = 0; i < lastCell; i++){
				//console.log(i, numberOfRow);
				if (numberOfRow*16+i === stackPointer){
					formatedRow += ` <mark>${row[i].toString(16).padStart(2,'0')}</mark>`;
				}
				else{
					formatedRow += ` ${row[i].toString(16).padStart(2,'0')}`;
				}
			}
			formatedRow += `</font></font></pre>`;
		}
		return formatedRow;

	}
	setInputFields(header: string){
		const style = "position:sticky;top: 0px;background-color: #403c3c;z-index: 2000;";
		const buttonHover = '<style>button:hover{cursor: pointer;}</style>';
		let entryFields = `<input type="text" size = "5" style = "margin-left: 60px;${style}" id="offset" placeholder="offset">
						   <input type="text" size = "6" style = "${style}" id="length" placeholder="length">`;
		const buttonHandler = `<script>
		const vscode = acquireVsCodeApi();
        const showButton = document.getElementById('show');
		const resetButton = document.getElementById('reset');
		const offSet = document.getElementById('offset')
		const len = document.getElementById('length')
		showButton?.addEventListener('click', function handleClick(event) {
			vscode.postMessage({command: 'show', offset: offSet.value, length: len.value})
		  });
		resetButton?.addEventListener('click', function handleClick(event) {
			vscode.postMessage({command: 'reset'})
		  });
    	</script>`;
		let showButton = `   <button id = "show", style = "position:sticky;top: 0px;border: 1px; height: 20px;"> Show memory segment${buttonHover}</button>`;
		let resetButton = `   <button id = "reset", style = "position:sticky;top: 0px;border: 1px; height: 20px"> Reset${buttonHover}</button>${buttonHandler}`;
		const container = `<div style = "position: sticky;top: 0px; left: 0px; width: 600px; height: 54px;background-color: #1e1e1e;z-index: 0;">${entryFields+showButton+resetButton+header}</div>`;
		return container;
	} 
	getHeader(){
		const headerStyle = `position:sticky;z-index: 2000;`;
		const header = `<div style = "${headerStyle}"><pre><b><font size = "4">      00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F</font></b></pre></div>`;
		return header;
	}
}