
[Setup]
    MinVersion=4.2.3,4.2.3
    AppName=PAGE - A Python GUI Generator
    AppId=PAGE - A Python GUI Generator
    CreateUninstallRegKey=1
    UsePreviousAppDir=1
    UsePreviousGroup=1
    AppVersion=3.5a
    AppVerName=PAGE - A Python GUI Generator 4.2.3
    BackColor=$FF0000
    BackColor2=$000000
    BackColorDirection=lefttoright
    WizardStyle=modern
    WindowShowCaption=1
    WindowStartMaximized=1
    WindowVisible=1
    WindowResizable=1
    UninstallLogMode=Append
    DirExistsWarning=auto
    UninstallFilesDir={app}
    DisableDirPage=0
    DisableStartupPrompt=0
    CreateAppDir=1
    DisableProgramGroupPage=0
    Uninstallable=1
    DefaultDirName=c:\page
    DefaultGroupName=PAGE
    AlwaysShowDirOnReadyPage=1
    EnableDirDoesntExistWarning=1
    ShowComponentSizes=1
    SourceDir=Z:\home\rozen\page
    OutputDir=Z:\home\rozen
    OutputBaseFilename=page-4.2.3


[Files]
    Source: Z:\home\rozen\page\*; DestDir: {app}; Flags: recursesubdirs
    
[Icons]
    Name: "{userdesktop}\PAGE"; Filename: "{app}\winpage.bat"; WorkingDir: "{app}"; IconFilename: "{app}\WIN_INSTALL\page.ico"; Flags: runminimized closeonexit
    Name: "{group}\PAGE"; Filename: "{app}\winpage.bat"; WorkingDir: "{app}"

	