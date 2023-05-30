import * as vscode from 'vscode';
import { CdmMemoryWebviewPanel } from './cdmMemoryWebviewPanel';
import * as path from 'path';


export class CdmMemoryViewProvider implements vscode.CustomTextEditorProvider {

	private static readonly viewType = 'cdmDebug.cdmMem';
	cdmWebview!: CdmMemoryWebviewPanel;
	webviewPanel!: vscode.WebviewPanel;
	resolveCustomTextEditor(document: vscode.TextDocument, webviewPanel: vscode.WebviewPanel, token: vscode.CancellationToken): void | Thenable<void> {
		this.cdmWebview = new CdmMemoryWebviewPanel(webviewPanel);
		webviewPanel.webview.options = {
			enableScripts: true,
		};
		this.webviewPanel = webviewPanel;
		this.webviewPanel.webview.html = this.cdmWebview.getWebviewContent(document.getText(), 0, 65536);
		this.registerDocumentChangeListener();
		this.subscriptOnDidReceiveMessage(document.getText());
	}
	
	subscriptOnDidReceiveMessage(documentContent: string){
		this.webviewPanel!.webview.onDidReceiveMessage(message => {
			switch (message.command){
				case 'show':
					const offset = parseInt(message.offset,16) | 0;
					let length = Number(message.length);
					if (message.length.length === 0){
						length = 65536;
					}
					this.webviewPanel.webview.html = this.cdmWebview.getWebviewContent(documentContent, offset, length);
					return;
				case 'reset':
					this.webviewPanel.webview.html = this.cdmWebview.getWebviewContent(documentContent, 0, 65536);
					return;}
		}, undefined, this.context.subscriptions);
	}
	

	
	public static register(context: vscode.ExtensionContext): vscode.Disposable {
		const provider = new CdmMemoryViewProvider(context);
		const providerRegistration = vscode.window.registerCustomEditorProvider(CdmMemoryViewProvider.viewType, provider);
		return providerRegistration;
	}

	constructor(
		private readonly context: vscode.ExtensionContext
	) {this.context = context;}
	registerDocumentChangeListener = () => {
		vscode.workspace.onDidChangeTextDocument(event => {
			const document = event.document;
			if (this.isCustomEditorDocument(document)) {
				this.webviewPanel!.webview.html = this.cdmWebview!.getWebviewContent(document.getText(), this.cdmWebview.offset, this.cdmWebview.length);
			}
		});
	};
	isCustomEditorDocument = (document: vscode.TextDocument): boolean => {
		if (path.extname(document.fileName) === '.cdmmem'){
			return true;
		}
		return false;
	};
}
