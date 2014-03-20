
[Setup]
    MinVersion=4.0,4.0
    AppName=PAGE - A Python GUI Generator
    AppId=PAGE - A Python GUI Generator
    CreateUninstallRegKey=1
    UsePreviousAppDir=1
    UsePreviousGroup=1
    AppVersion=3.5
    AppVerName=PAGE - A Python GUI Generator 3.5
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
    DefaultGroupName=
    AlwaysShowDirOnReadyPage=1
    EnableDirDoesntExistWarning=1
    ShowComponentSizes=1
    SourceDir=C:\pkg\page
    OutputDir=C:\pkg
    OutputBaseFilename=page-3.5


[Files]
    Source: C:\pkg\page\*; DestDir: {app}; Flags: recursesubdirs
    
[Icons]
    Name: "{userdesktop}\PAGE"; Filename: "{app}\winpage.bat"; WorkingDir: "{app}"; IconFilename: "{app}\WIN_INSTALL\page.ico"; Flags: runminimized closeonexit
    

