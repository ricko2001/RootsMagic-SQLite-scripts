import os


FileInPath = r"C:\Users\rotter\Documents\Genealogy\GeneDB\Exhibits\Sources\Grave Marker\Waldzell"
FileInName = r"Friedhof Waldzell Grave List.txt"
FileOutFldrName = "Generated files"


EntrySeperator = "======================================\n"   # 38 equals
tempFileName = "trashFile"
pathSep = '\\'
FileOutExt = ".txt"
FileOutPath= FileInPath + pathSep + FileOutFldrName

fileIn = open(FileInPath + pathSep + FileInName, 'r', encoding='utf-8-sig')
prevFileOut = open(FileOutPath + pathSep + tempFileName + FileOutExt, 'w')
FileOut = prevFileOut

Line = fileIn.readline() 
while (Line != ""):
    print (Line)
    if (Line == EntrySeperator):
        FileOut.write( EntrySeperator )
        Line = fileIn.readline() 
        FileOutName=Line.rstrip('\n')
        if (Line == EntrySeperator):
            FileOutName = tempFileName
        prevFileOut.close()
        FileOut = open (FileOutPath + pathSep + FileOutName + FileOutExt, 'w', encoding='utf-8-sig')
        prevOutFile = FileOut
        FileOut.write(EntrySeperator)
    FileOut.write(Line)
    Line = fileIn.readline() 

fileIn.close()
FileOut.close() 
prevFileOut.close()
os.remove (FileOutPath + pathSep + tempFileName + FileOutExt)

input("Press Enter to continue.")

