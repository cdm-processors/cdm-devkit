#####################################################
#                                                   #
#   This Makefile builds all projects and puts      #
#   distribution files in BUILD_FOLDER.              #
#                                                   #
#####################################################

# Folder paths
JAVA_PROJECTS_FOLDER = logisim
VSCODE_EXTENSION_FOLDER = vscode-cdm-extension
PYTHON_DIST_FOLDER = dist
EXAMPLES_FOLDER = examples
PROCESSOR_SCHEMES_FOLDER = logisim
BUILD_FOLDER = build


# Build folder path
BUILD_FOLDER_EXIST = $(wildcard $(BUILD_FOLDER))


# Enabled Java projects
JAVA_PROJECTS = logisim-banked-memory logisim-cdm-emulator

# Enables processors
PROCESSORS = cdm8e cdm16

# Distribution archive files
ARCHIVE_FILES = *.circ jar examples

# System-independent commands
POETRY = poetry
VSCE = vsce
CD = cd
MKDIR = mkdir
SYNTHM = synthm

ifeq ($(OS), Windows_NT)

# Windows-specific commands

GRADLEW = .\gradlew.bat
CP = xcopy /s /y
RM = rmdir /s /q
RM_FILE = del /q
ZIP = zip -r

# Check for tar archiver on Windows
ifneq ($(shell where tar),)
TAR = tar -czvf
else
TAR = echo No TAR
endif

CURRENT_DIR = $(shell cd)

SLASH = \\

else

# Unix-specific commands

GRADLEW = ./gradlew
CP = cp -r
RM = rm -r
RM_FILE = rm
TAR = tar -czvf

# Check for zip archiver on Unix
ifneq ($(shell which zip),)
ZIP = zip -r
else
ZIP = echo No ZIP
endif

# Command that sets permissions for ./gradlew scripts
SET_PERMISSIONS = find . -name "gradlew" -exec chmod +x {} \;

CURRENT_DIR = $(shell pwd)

SLASH = /

endif

# Macro that puts new line char ('\n')
define NEW_LINE


endef


#####################################################
#                                                   #
#                      Targets                      #
#                                                   #
#####################################################

.PHONY: all dist $(BUILD_FOLDER_EXIST)

# Build all projects and create distribution package
dist: all | $(BUILD_FOLDER_EXIST)

	@echo ---------------------------
	@echo Making distribution package
	@echo ---------------------------

	$(MKDIR) $(BUILD_FOLDER)

	$(CP) $(PYTHON_DIST_FOLDER)$(SLASH)* $(BUILD_FOLDER)

	$(MKDIR) $(BUILD_FOLDER)$(SLASH)jar

	$(foreach PROJECT, $(JAVA_PROJECTS), \
		$(CP) $(JAVA_PROJECTS_FOLDER)$(SLASH)$(PROJECT)$(SLASH)build$(SLASH)libs$(SLASH)*.jar \
		      $(BUILD_FOLDER)$(SLASH)jar $(NEW_LINE) \
	)

	$(CP) $(VSCODE_EXTENSION_FOLDER)$(SLASH)vscode-cdm-extension-*.*.*.vsix $(BUILD_FOLDER)

	$(MKDIR) $(BUILD_FOLDER)$(SLASH)examples

	$(CP) $(EXAMPLES_FOLDER)$(SLASH)* $(BUILD_FOLDER)$(SLASH)examples$(SLASH)

	$(foreach PROCESSOR, $(PROCESSORS), \
		$(CP) $(PROCESSOR_SCHEMES_FOLDER)$(SLASH)$(PROCESSOR)$(SLASH)*.circ $(BUILD_FOLDER) $(NEW_LINE) \
	)

	$(CD) $(BUILD_FOLDER) && $(ZIP) cdm-devkit-misc-$(VERSION).zip $(ARCHIVE_FILES)

	$(CD) $(BUILD_FOLDER) && $(TAR) cdm-devkit-misc-$(VERSION).tar.gz $(ARCHIVE_FILES)

# Remove build/ if exists
$(BUILD_FOLDER_EXIST):
	$(RM) $(BUILD_FOLDER)

# Build all projects
all: java python vscode

# Build Java-based projects
java: emulator_resources gradlew

	@echo ----------------------
	@echo Building Java projects
	@echo ----------------------

	$(foreach PROJECT, $(JAVA_PROJECTS), \
		$(CD) $(CURRENT_DIR)$(SLASH)$(JAVA_PROJECTS_FOLDER)$(SLASH)$(PROJECT) && \
		$(GRADLEW) jar -Pversion="$(VERSION)" $(NEW_LINE) \
	)

# Set +x permissions for ./gradlew scripts
gradlew:
	$(SET_PERMISSIONS)

# Build Python-based projects
python:
	@echo ------------------------
	@echo Building Python projects
	@echo ------------------------

	$(POETRY) version $(VERSION)
	$(POETRY) build

# Build VS Code extension
vscode:
	@echo --------------------------
	@echo Building VS Code Extension
	@echo --------------------------

	$(CD) $(CURRENT_DIR)$(SLASH)$(VSCODE_EXTENSION_FOLDER) && $(VSCE) package $(VERSION)

# Compile microcode from CdM-16
microcode:
	$(CD) $(CURRENT_DIR)$(SLASH)$(JAVA_PROJECTS_FOLDER)$(SLASH)cdm16$(SLASH)microcode && \
		$(SYNTHM) -i cdm16_decoder.def $(NEW_LINE)

	$(CD) $(CURRENT_DIR)$(SLASH)$(JAVA_PROJECTS_FOLDER)$(SLASH)cdm16$(SLASH)microcode && \
		$(SYNTHM) -i cdm16_decoder_exc.def --fill 0x8000400 $(NEW_LINE)

# Prepare resources for logisim-cdm-emulator
emulator_resources: microcode
	$(CP) $(PROCESSOR_SCHEMES_FOLDER)$(SLASH)cdm16$(SLASH)microcode$(SLASH)cdm16_decoder*.img \
		$(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-cdm-emulator$(SLASH)src$(SLASH)main$(SLASH)resources

clean: clean_microcode clean_emulator_resources
	$(RM) $(BUILD_FOLDER)

	$(RM) $(PYTHON_DIST_FOLDER)

	$(foreach PROJECT, $(JAVA_PROJECTS), \
		$(RM) $(JAVA_PROJECTS_FOLDER)$(SLASH)$(PROJECT)$(SLASH)build \
			  $(JAVA_PROJECTS_FOLDER)$(SLASH)$(PROJECT)$(SLASH).gradle $(NEW_LINE) \
	)

	$(RM_FILE) $(VSCODE_EXTENSION_FOLDER)$(SLASH)vscode-cdm-extension-*.*.*.vsix

clean_microcode:
	$(RM_FILE) \
		$(JAVA_PROJECTS_FOLDER)$(SLASH)cdm16$(SLASH)microcode$(SLASH)cdm16_decoder.circ \
		$(JAVA_PROJECTS_FOLDER)$(SLASH)cdm16$(SLASH)microcode$(SLASH)cdm16_decoder.img

	$(RM_FILE) \
		$(JAVA_PROJECTS_FOLDER)$(SLASH)cdm16$(SLASH)microcode$(SLASH)cdm16_decoder_exc.circ \
		$(JAVA_PROJECTS_FOLDER)$(SLASH)cdm16$(SLASH)microcode$(SLASH)cdm16_decoder_exc.img

clean_emulator_resources:
	$(RM_FILE) \
		$(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-cdm-emulator$(SLASH)src$(SLASH)main$(SLASH)resources$(SLASH)*.img

# Tests

# Runner jar folder path
RUNNER_FOLDER = tests$(SLASH)jar

# Prepare test environment
prepare_tests: prepare_tests_processors prepare_tests_emulator gradlew
	$(CD) $(CURRENT_DIR)$(SLASH)$(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-banked-memory && \
		$(GRADLEW) jar -Pversion="$(VERSION)" $(NEW_LINE)

	$(CP) $(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-banked-memory$(SLASH)build$(SLASH)libs$(SLASH)*.jar \
		$(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-runner$(SLASH)libs

	$(CD) $(CURRENT_DIR)$(SLASH)$(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-runner && \
		$(GRADLEW) shadowJar -Pversion="$(VERSION)" $(NEW_LINE)

	$(CP) $(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-runner$(SLASH)build$(SLASH)libs$(SLASH)*.jar \
		$(RUNNER_FOLDER)

	$(foreach PROCESSOR, $(PROCESSORS), \
		$(CP) $(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-banked-memory$(SLASH)build$(SLASH)libs$(SLASH)*.jar \
		 	tests$(SLASH)resources$(SLASH)$(PROCESSOR)$(SLASH)circuits $(NEW_LINE) \
	)

prepare_tests_processors:
	$(foreach PROCESSOR, $(PROCESSORS), \
		$(CP) $(PROCESSOR_SCHEMES_FOLDER)$(SLASH)$(PROCESSOR)$(SLASH)*.circ \
		 	tests$(SLASH)resources$(SLASH)$(PROCESSOR)$(SLASH)circuits $(NEW_LINE) \
	)

prepare_tests_emulator: emulator_resources gradlew
	$(CD) $(CURRENT_DIR)$(SLASH)$(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-cdm-emulator && \
		$(GRADLEW) jar -Pversion="$(VERSION)" $(NEW_LINE)

	$(CP) $(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-cdm-emulator$(SLASH)build$(SLASH)libs$(SLASH)*.jar \
		tests$(SLASH)resources$(SLASH)cdm16$(SLASH)circuits


# Clean test environment
clean_tests: clean_tests_processors clean_tests_emulator
	$(RM) $(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-banked-memory$(SLASH)build \
		$(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-banked-memory$(SLASH).gradle $(NEW_LINE)

	$(RM_FILE) $(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-runner$(SLASH)libs$(SLASH)logisim-banked-memory*

	$(RM) $(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-runner$(SLASH)build \
		$(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-runner$(SLASH).gradle $(NEW_LINE)

	$(RM_FILE) $(RUNNER_FOLDER)$(SLASH)*.jar

	$(foreach PROCESSOR, $(PROCESSORS), \
		$(RM_FILE) tests$(SLASH)resources$(SLASH)$(PROCESSOR)$(SLASH)circuits$(SLASH)logisim-banked-memory* $(NEW_LINE) \
	)

clean_tests_processors:
	$(RM_FILE) tests$(SLASH)resources$(SLASH)cdm8e$(SLASH)circuits$(SLASH)CdM-8e.circ
	$(RM_FILE) tests$(SLASH)resources$(SLASH)cdm16$(SLASH)circuits$(SLASH)cdm16.circ

clean_tests_emulator: clean_microcode clean_emulator_resources
	$(RM) $(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-cdm-emulator$(SLASH)build \
		$(JAVA_PROJECTS_FOLDER)$(SLASH)logisim-cdm-emulator$(SLASH).gradle $(NEW_LINE)

	$(RM_FILE) tests$(SLASH)resources$(SLASH)cdm16$(SLASH)circuits$(SLASH)logisim-cdm-emulator*
