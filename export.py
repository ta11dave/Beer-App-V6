#shamelessly steal the vba module and convert to python
import recipes

filename = "blah.xml"
myfile = open(filename, "w+")

#myfile.write("<?xml version=" & Chr(34) & "1.0" & Chr(34) & " encoding=" & Chr(34) & "ISO-8859-1" & Chr(34) & "?>")
myfile.write("<RECIPES>")

for aRecipe in recipes.recipes:
	#for each recipe in the array recipes.
	myfile.write("<RECIPE>")
	myfile.write("<NAME></NAME>")
	myfile.write("<VERSION>1</VERSION>")
	myfile.write("<TYPE></TYPE>")
	myfile.write("<BREWER></BREWER>")
	myfile.write("<BATCH_SIZE></BATCH_SIZE>")
	myfile.write("<BOIL_SIZE></BOIL_SIZE>")
	myfile.write("<BOIL_TIME></BOIL_TIME>")
	myfile.write("<EFFICIENCY>""</EFFICIENCY>")
	myfile.write("<TASTE_NOTES>""</TASTE_NOTES>")

	myfile.write("<STYLE>")
	myfile.write("<NAME></NAME>")
	myfile.write("<CATEGORY></CATEGORY>")
	myfile.write("<VERSION>1</VERSION>")
	myfile.write("<STYLE_GUIDE></STYLE_GUIDE>")
	myfile.write("<TYPE></TYPE>")
	myfile.write("<OG_MIN></OG_MIN>")
	myfile.write("<OG_MAX></OG_MAX>")
	myfile.write("<FG_MIN></FG_MIN>")
	myfile.write("<FG_MAX></FG_MAX>")
	myfile.write("<IBU_MIN></IBU_MIN>")
	myfile.write("<IBU_MAX></IBU_MAX>")
	myfile.write("<COLOR_MIN></COLOR_MIN>")
	myfile.write("<COLOR_MAX></COLOR_MAX>")
	myfile.write("<ABV_MIN></ABV_MIN>")
	myfile.write("<ABV_MAX></ABV_MAX>")
	myfile.write("</STYLE>")

	#For the mash
	myfile.write("<MASH>")
	myfile.write("<NAME>s Mash Schedule</NAME>")
	myfile.write("<VERSION>1</VERSION>")
	myfile.write("<MASH_STEPS>")

	#log the mash steps
	myfile.write("<MASH_STEP>")
	myfile.write("<NAME></NAME>")
	myfile.write("<VERSION>1</VERSION>")

	myfile.write("<TYPE>Infusion</TYPE>")
	myfile.write("<INFUSE_AMOUNT></INFUSE_AMOUNT>")
	myfile.write("<STEP_TEMP></STEP_TEMP>")
	myfile.write("<STEP_TIME></STEP_TIME>")
	myfile.write("</MASH_STEP>")
	myfile.write("</MASH_STEPS>")
	myfile.write("</MASH>")



	#For entering the hops
	myfile.write("<HOPS>")

	#for each hop
	#log the hop
	#If MyCell.Value != "Empty":
	myfile.write("<HOP>")
	myfile.write("<NAME></NAME>")
	myfile.write("<VERSION>1</VERSION>")
	myfile.write("<ALPHA></ALPHA>")
	myfile.write("<AMOUNT></AMOUNT>")
	myfile.write("<USE></USE>")
	#if "Use" = "Dry Hop":
	myfile.write("<TIME></TIME>")
	myfile.write("<DISPLAY_AMOUNT> oz</DISPLAY_AMOUNT>")
	myfile.write("</HOP>")
	myfile.write("</HOPS>")

	#For entering the malts
	myfile.write("<FERMENTABLES>")

	#for each fermentable
	#log the malt
	#if MyCell.Value != "Empty":
	myfile.write("<FERMENTABLE>")
	myfile.write("<NAME></NAME>")
	myfile.write("<VERSION>1</VERSION>")
	myfile.write("<TYPE>Grain</TYPE>")
	myfile.write("<AMOUNT></AMOUNT>")
	myfile.write("<YIELD></YIELD>")
	myfile.write("<COLOR></COLOR>")
	myfile.write("<ORIGIN></ORIGIN>")

	myfile.write("</FERMENTABLE>")
	#next
	myfile.write("</FERMENTABLES>")

	#Start Misc Additions
	myfile.write("<MISCS>")

	#For Each MyCell In Range(MiscRng)
	#log the adjuncts
	#if MyCell.Value <> "Empty" Then
	myfile.write("<MISC>")
	myfile.write("<NAME></NAME>")
	myfile.write("<VERSION>1</VERSION>")
	myfile.write("<TYPE></TYPE>")
	myfile.write("<USE></USE>")
	myfile.write("<AMOUNT></AMOUNT>") #g or L; idk which
	myfile.write("<AMOUNT_IS_WEIGHT>TRUE</AMOUNT_IS_WEIGHT>")
	myfile.write("<TIME></TIME>")
	myfile.write("<NOTES></NOTES>")
	myfile.write("</MISC>")
	myfile.write("</MISCS>")

	#Yeast
	myfile.write("<YEASTS>")
	myfile.write("<YEAST>")
	myfile.write("<NAME></NAME>")
	myfile.write("<VERSION>1</VERSION>")
	myfile.write("<TYPE></TYPE>")
	myfile.write("<FORM></FORM>")
	myfile.write("<AMOUNT>1</AMOUNT>") #lol deal with it
	myfile.write("<LABORATORY></LABORATORY>")
	myfile.write("<PRODUCT_ID></PRODUCT_ID>")
	myfile.write("<MIN_TEMPERATURE></MIN_TEMPERATURE>")
	myfile.write("<MAX_TEMPERATURE></MAX_TEMPERATURE>")
	myfile.write("<FLOCCULATION></FLOCCULATION>")
	myfile.write("<ATTENUATION></ATTENUATION>")
	myfile.write("</YEAST>")
	myfile.write("</YEASTS>")

	#Water
	myfile.write("<WATERS>")
	myfile.write("<WATER>")
	myfile.write("<NAME></NAME>")
	myfile.write("<VERSION>1</VERSION>")
	myfile.write("<AMOUNT></AMOUNT>")
	myfile.write("<CALCIUM></CALCIUM>")
	myfile.write("<BICARBONATE></BICARBONATE>")
	myfile.write("<SULFATE></SULFATE>")
	myfile.write("<CHLORIDE></CHLORIDE>")
	myfile.write("<SODIUM></SODIUM>")
	myfile.write("<MAGNESIUM></MAGNESIUM>")
	myfile.write("</WATER>")
	myfile.write("</WATERS>")

	#End
	myfile.write("</RECIPE>")
myfile.write("</RECIPES>")


"""
'For an example
'http://www.beerxml.com/recipes.xml

'How to is here
'http://www.beerxml.com/beerxml.htm

'Get active sheet
sheetNo = ActiveSheet.Index

'Update adjuncts, and then the metric side so they're the same
For Each cell In Worksheets(7).Range("E51:E54")
    If InStr(cell, "day") <> 0 Then
        Cells(cell.Row, 5) = Mid(cell.Value, 1, InStr(cell, "day") - 2) * 1440
    End If
Next

'Make sure the GUI tab is selected
Worksheets(1).Activate

'Create file to export to
SavedFile = Application.DefaultFilePath & "\" & Range("D9").Value & ".xml"
TextFile = FreeFile
Open SavedFile For Output As TextFile

'Start
Print("<?xml version=" & Chr(34) & "1.0" & Chr(34) & " encoding=" & Chr(34) & "ISO-8859-1" & Chr(34) & "?>"
Print("<RECIPES>"
Print("<RECIPE>"
Dim VERSION As Integer
VERSION = 1

'Get yeast ID
Dim i As Integer
For Each yeast In Worksheets(5).Range("A2:A456")
  If Worksheets(5).Cells(yeast.Row, 1) = Range("H51") & " && " & Range("G51") Then
    YeastID = yeast.Row
  End If
Next

'Recipe Info
Print("<NAME>" + Range("D9").Value + "</NAME>"
Print("<VERSION>" & VERSION & "</VERSION>"
Print("<TYPE>" & Range("E9").Value & "</TYPE>"
Print("<BREWER>" & Range("D8").Value & "</BREWER>"
Print("<BATCH_SIZE>" & (Range("D12").Value * 3.78541) & "</BATCH_SIZE>"
Print("<BOIL_SIZE>" & (Range("D11").Value * 3.78541) & "</BOIL_SIZE>"
Print("<BOIL_TIME>" & "60" & "</BOIL_TIME>"
Print("<EFFICIENCY>" & Range("D17").Value * 100 & "</EFFICIENCY>"
Print("<TASTE_NOTES>" & Range("C79") & "</TASTE_NOTES>"

'Searching for style
StyleRow = 4
Found = False
While Found = False
If Range("D10") <> Worksheets(2).Range("B" & StyleRow) Then
StyleRow = StyleRow + 1
Else
Found = True
End If
Wend

'Adding Style
Print("<STYLE>"
Print("<NAME>" & Range("D10").Value & "</NAME>"
Print("<CATEGORY>" & Worksheets(2).Cells(StyleRow, 6).Value & "</CATEGORY>"
Print(<VERSION>" & VERSION & "</VERSION>"
If IsError(Worksheets(2).Cells(StyleRow, 3).Value) = True Then
    Print(<CATEGORY_NUMBER>XX</CATEGORY_NUMBER>"
Else
    Print(<CATEGORY_NUMBER>" & Worksheets(2).Cells(StyleRow, 3).Value & "</CATEGORY_NUMBER>"
End If
If IsError(Worksheets(2).Cells(StyleRow, 4).Value) = True Then
    Print(<STYLE_LETTER>XX</STYLE_LETTER>"
Else
    Print(<STYLE_LETTER>" & Worksheets(2).Cells(StyleRow, 3).Value & "</STYLE_LETTER>"
End If
Print(<STYLE_GUIDE>" & Worksheets(2).Cells(StyleRow, 15).Value & "</STYLE_GUIDE>"
Print(<TYPE>" & Worksheets(5).Cells(YeastID, 5).Value & "</TYPE>"
Print(<OG_MIN>" & Worksheets(2).Cells(StyleRow, 7).Value & "</OG_MIN>"
Print(<OG_MAX>" & Worksheets(2).Cells(StyleRow, 8).Value & "</OG_MAX>"
Print(<FG_MIN>" & Worksheets(2).Cells(StyleRow, 9).Value & "</FG_MIN>"
Print(<FG_MAX>" & Worksheets(2).Cells(StyleRow, 10).Value & "</FG_MAX>"
Print(<IBU_MIN>" & Worksheets(2).Cells(StyleRow, 13).Value & "</IBU_MIN>"
Print(<IBU_MAX>" & Worksheets(2).Cells(StyleRow, 14).Value & "</IBU_MAX>"
Print(<COLOR_MIN>" & Worksheets(2).Cells(StyleRow, 15).Value & "</COLOR_MIN>"
Print(<COLOR_MAX>" & Worksheets(2).Cells(StyleRow, 16).Value & "</COLOR_MAX>"
Print(<ABV_MIN>" & Worksheets(2).Cells(StyleRow, 11).Value & "</ABV_MIN>"
Print(<ABV_MAX>" & Worksheets(2).Cells(StyleRow, 12).Value & "</ABV_MAX>"
Print("</STYLE>"


'For the mash
Print("<MASH>"
MashRng = "G14:G19"
Print("<NAME>" & Range("D8").Value & Chr(39) & "s Mash Schedule</NAME>"
Print("<VERSION>" & VERSION & "</VERSION>"
Print("<MASH_STEPS>"

For Each MyCell In Range(MashRng)
'log the mash steps
If MyCell.Value <> "Empty" Then
Print("<MASH_STEP>"
Print("<NAME>" & Cells(MyCell.Row, 7).Value & "</NAME>"
Print("<VERSION>" & VERSION & "</VERSION>"

If Cells(MyCell.Row, 10).Value = "Y" Then
Print("<TYPE>Decoction</TYPE>"
ElseIf (Cells(MyCell.Row, 7).Value = "Mash Out") Or (Cells(MyCell.Row, 7).Value = "Mash In") Then
Print("<TYPE>Temperature</TYPE>"
Else
Print("<TYPE>Infusion</TYPE>"
End If

If Range("G21").Value = 0 Then
Print("<INFUSE_AMOUNT>" & Range("H5").Value & "</INFUSE_AMOUNT>"
Else
Print("<INFUSE_AMOUNT>" & Cells(MyCell.Row + 116, MyCell.Column).Value & "</INFUSE_AMOUNT>"
End If

Print("<STEP_TEMP>" & (5 / 9) * (Cells(MyCell.Row, 9).Value - 32) & "</STEP_TEMP>"
Print("<STEP_TIME>" & Cells(MyCell.Row, 8).Value & "</STEP_TIME>"
Print("</MASH_STEP>"
End If
Next
Print("</MASH_STEPS>"
Print("</MASH>"



'For entering the hops
Print("<HOPS>"
HopRng = "D38:D48"

For Each MyCell In Range(HopRng)
'log the hop
If MyCell.Value <> "Empty" Then
Print("<HOP>"
Print("<NAME>" & Cells(MyCell.Row, 4).Value & "</NAME>"
Print("<VERSION>" & VERSION & "</VERSION>"
Print("<ALPHA>" & Cells(MyCell.Row, 8).Value & "</ALPHA>"
Print("<AMOUNT>" & (Cells(MyCell.Row, 5).Value * 0.02835) & "</AMOUNT>"
Print("<USE>" & Cells(MyCell.Row, 6).Value & "</USE>"
If Cells(MyCell.Row, 6).Value = "Dry Hop" Then
Print("<TIME>" & Cells(MyCell.Row, 3).Value * 3360 & "</TIME>"
Else
Print("<TIME>" & Cells(MyCell.Row, 3).Value & "</TIME>"
End If
Print("<DISPLAY_AMOUNT>" & Cells(MyCell.Row, 5).Value & " oz</DISPLAY_AMOUNT>"

Print("</HOP>"
End If
Next
Print("</HOPS>"

'For entering the malts
Print("<FERMENTABLES>"
MaltRng = "E25:E35"

For Each MyCell In Range(MaltRng)
'log the malt
If MyCell.Value <> "Empty" Then
Print("<FERMENTABLE>"

Print("<NAME>" & Cells(MyCell.Row, 5).Value & "</NAME>"
Print("<VERSION>" & VERSION & "</VERSION>"
Print("<TYPE>Grain</TYPE>"
Print("<AMOUNT>" & (Cells(MyCell.Row, 3).Value + Cells(MyCell.Row, 4).Value / 16) / 2.2 & "</AMOUNT>"
Print("<YIELD>" & Cells(MyCell.Row, 7).Value & "</YIELD>"
Print("<COLOR>" & Cells(MyCell.Row, 6).Value & "</COLOR>"
Print("<ORIGIN>" & vlookupVBA(Cells(MyCell.Row, 2).Value, Range("fermentables!A4:I174"), 2) & "</ORIGIN>"

Print("</FERMENTABLE>"
End If
Next
Print("</FERMENTABLES>"

'Start Misc Additions
Print("<MISCS>"
MiscRng = "D51:D54"

For Each MyCell In Range(MiscRng)
'log the adjuncts
If MyCell.Value <> "Empty" Then

Print("<MISC>"
Print("<NAME>" & MyCell.Value & "</NAME>"
Print("<VERSION>" & VERSION & "</VERSION>"
Print("<TYPE></TYPE>"
Print("<USE></USE>"
Print("<AMOUNT>" & Cells(MyCell.Row, 3).Value & "</AMOUNT>" 'g or L; idk which
Print("<AMOUNT_IS_WEIGHT>TRUE</AMOUNT_IS_WEIGHT>"
Print("<TIME>" & Cells(MyCell.Row, 5).Value & "</TIME>"
Print("<NOTES></NOTES>"
Print("</MISC>"

End If
Next
Print("</MISCS>"

'Yeast
Print("<YEASTS>"
Print("<YEAST>"
Print("<NAME>" & Worksheets(5).Cells(YeastID, 2).Value & "</NAME>"
Print("<VERSION>" & VERSION & "</VERSION>"
Print("<TYPE>" & Worksheets(5).Cells(YeastID, 5).Value & "</TYPE>"
If (Worksheets(5).Cells(YeastID, 3).Value = "Danstar") Or (Worksheets(5).Cells(YeastID, 3).Value = "Fermentis / Safale") Or (Worksheets(5).Cells(YeastID, 3).Value = "Mangrove Jack") Then
Print("<FORM>Dry</FORM>"
Else
Print("<FORM>Liquid</FORM>"
End If
Print("<AMOUNT>1</AMOUNT>" 'lol deal with it
Print("<LABORATORY>" & Worksheets(5).Cells(YeastID, 3).Value & "</LABORATORY>"
Print("<PRODUCT_ID>" & Worksheets(5).Cells(YeastID, 4).Value & "</PRODUCT_ID>"
Print("<MIN_TEMPERATURE>" & Worksheets(5).Cells(YeastID, 9).Value & "</MIN_TEMPERATURE>"
Print("<MAX_TEMPERATURE>" & Worksheets(5).Cells(YeastID, 10).Value & "</MAX_TEMPERATURE>"
Print("<FLOCCULATION>" & Worksheets(5).Cells(YeastID, 7).Value & "</FLOCCULATION>"
Print("<ATTENUATION>" & Worksheets(5).Cells(YeastID, 8).Value & "</ATTENUATION>"
Print("</YEAST>"
Print("</YEASTS>"

'Water
Print("<WATERS>"
Print("<WATER>"
Print("<NAME>" & Worksheets(6).Range("B2").Value & "</NAME>"
Print("<VERSION>" & VERSION & "</VERSION>"
Print("<AMOUNT>" & Range("D11").Value * 4.54609 & "</AMOUNT>"
Print("<CALCIUM>" & Worksheets(6).Range("B6").Value & "</CALCIUM>"
Print("<BICARBONATE>" & Worksheets(6).Range("G6").Value & "</BICARBONATE>"
Print("<SULFATE>" & Worksheets(6).Range("D6").Value & "</SULFATE>"
Print("<CHLORIDE>" & Worksheets(6).Range("F6").Value & "</CHLORIDE>"
Print("<SODIUM>" & Worksheets(6).Range("E6").Value & "</SODIUM>"
Print("<MAGNESIUM>" & Worksheets(6).Range("C6").Value & "</MAGNESIUM>"
Print("</WATER>"
Print("</WATERS>"

'End
Print("</RECIPE>"
Print("</RECIPES>"

Close #TextFile

'Update adjuncts back, and then the metric side so they're the same
For Each cell In Worksheets(7).Range("E51:E54")
    If cell > 200 Then
        Cells(cell.Row, 5) = Cells(cell.Row, 5) / 1440 & " day(s)"
    End If
Next

'Go back to sheet you triggered macro from
Worksheets(sheetNo).Activate

MsgBox "Saved at " & SavedFile

End Sub
"""
