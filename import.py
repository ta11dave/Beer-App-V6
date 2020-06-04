#shamelessly steal the vba module and convert to python
#give option to load ALL recipes
import recipes as rp
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#get file from tk file picker
Tk().withdraw()
filename = askopenfilename()
datasource = open(filename)

# parse an open file
mydoc = parse(datasource)

#for each recipe in the file
#make a new recipe instance
"""

'Works but won't work for other programs' files
'MsgBox root.ChildNodes(9).ChildNodes(0).Text

'Only taking the first recipe
'MsgBox root.ChildNodes(3).Text

'get recipe basic info
i = 0
While i < root.ChildNodes.Length
  
  If root.ChildNodes(i).tagName = "NAME" Then
  '<NAME>LAGAH</NAME>
  Range("D9") = root.ChildNodes(i).Text
  End If
  
  'Who cares?
  '<VERSION>1</VERSION>
  
  If root.ChildNodes(i).tagName = "TYPE" Then
  '<TYPE>BIAB</TYPE>
  Range("E9") = root.ChildNodes(i).Text
  End If
  
  If root.ChildNodes(i).tagName = "BREWER" Then
  '<BREWER>Dave</BREWER>
  Range("D8") = root.ChildNodes(i).Text
  End If
  
  If root.ChildNodes(i).tagName = "BATCH_SIZE" Then
  '<BATCH_SIZE>25.003495</BATCH_SIZE>
  Range("D12") = root.ChildNodes(i).Text
  End If
  
  'If root.ChildNodes(i).tagName = "BOIL_SIZE" Then
  '<BOIL_SIZE>29.549585</BOIL_SIZE>
  'Range("D11") = root.ChildNodes(i).Text
  'End If
  'Currently calculated
  
  If root.ChildNodes(i).tagName = "BOIL_TIME" Then
  '<BOIL_TIME>60</BOIL_TIME>
  Range("J9") = root.ChildNodes(i).Text
  End If
  
  If root.ChildNodes(i).tagName = "EFFICIENCY" Then
  '<EFFICIENCY>0.75</EFFICIENCY>
  Range("D17") = root.ChildNodes(i).Text / 100
  End If
  
  If root.ChildNodes(i).tagName = "NOTES" Then
  '<NOTES/>
  Range("C79") = root.ChildNodes(i).Text
  End If
  
  'get assign style
  
  If root.ChildNodes(i).tagName = "STYLE" Then
  j = 0
  k = 4
  'See if style exists *** DONE
  While (root.ChildNodes(i).ChildNodes(0).Text <> Worksheets(2).Range("B" & k)) And (k < 120)
  k = k + 1
  Wend
    If Worksheets(2).Range("B" & k) <> Empty Then
      Range("D10") = Worksheets(2).Range("B" & k)
    Else
    'And if it doesn't exist?
      MsgBox "Not a BJCP Style..."
      '<NAME>American Lager</NAME>
      '<CATEGORY>Standard American Beer</CATEGORY>
      '<VERSION>1</VERSION>
      '<CATEGORY_NUMBER>1</CATEGORY_NUMBER>
      '<STYLE_LETTER>B</STYLE_LETTER>
      '<STYLE_GUIDE>BJCP</STYLE_GUIDE>
      '<TYPE>Lager</TYPE>
      '<OG_MIN>1.04</OG_MIN>
      '<OG_MAX>1.05</OG_MAX>
      '<FG_MIN>1.004</FG_MIN>
      '<FG_MAX>1.01</FG_MAX>
      '<IBU_MIN>8</IBU_MIN>
      '<IBU_MAX>18</IBU_MAX>
      '<COLOR_MIN>2</COLOR_MIN>
      '<COLOR_MAX>4</COLOR_MAX>
      '<ABV_MIN>0.043</ABV_MIN>
      '<ABV_MAX>0.053</ABV_MAX>
    End If
  End If
  
  
  If root.ChildNodes(i).tagName = "MASH" Then
  'get/assign mash *** DONE
  j = 0
  k = 0
  l = 0 ' the count of the number of recorded mash steps
  Dim MashRow As Integer
  Dim MashMod As Boolean
  MashRow = 14
  MashMod = False
  While (j < root.ChildNodes(i).ChildNodes.Length) 'still in the mash
    If root.ChildNodes(i).ChildNodes(j).tagName = "MASH_STEPS" Then
    k = 0
    If l >= root.ChildNodes(i).ChildNodes(j).ChildNodes.Length Then 'when you run out of mash steps
    GoTo MashEnd
    End If
      While k < root.ChildNodes(i).ChildNodes(j).ChildNodes(l).ChildNodes.Length 'for each mash property
        If root.ChildNodes(i).ChildNodes(j).ChildNodes(l).ChildNodes(k).tagName = "TYPE" Then
          If root.ChildNodes(i).ChildNodes(j).ChildNodes(l).ChildNodes(k).Text = "Infusion" Then
            Range("G" & MashRow) = "Saccharification"
            Range("J" & MashRow) = "N"
            MashMod = True
          End If
          If root.ChildNodes(i).ChildNodes(j).ChildNodes(l).ChildNodes(k).Text = "Temperature" Then
            If MashRow = 14 Then
              Range("G" & MashRow) = "Mash In"
              MashMod = True
            Else
              Range("G" & MashRow) = "Mash Out"
              MashMod = True
            End If
          End If
          If root.ChildNodes(i).ChildNodes(j).ChildNodes(l).ChildNodes(k).Text = "Decoction" Then
            Range("G" & MashRow) = "Saccharification"
            Range("J" & MashRow) = "Y"
            MashMod = True
          End If
        End If
        If root.ChildNodes(i).ChildNodes(j).ChildNodes(l).ChildNodes(k).tagName = "STEP_TEMP" Then
          Range("I" & MashRow) = Round(root.ChildNodes(i).ChildNodes(j).ChildNodes(l).ChildNodes(k).Text, 0)
          MashMod = True
        End If
        If root.ChildNodes(i).ChildNodes(j).ChildNodes(l).ChildNodes(k).tagName = "STEP_TIME" Then
          Range("H" & MashRow) = root.ChildNodes(i).ChildNodes(j).ChildNodes(l).ChildNodes(k).Text
          MashMod = True
        End If
        k = k + 1
      Wend
    l = l + 1
    If MashMod = True Then
      MashRow = MashRow + 1
      MashMod = False
    End If
    Else
    j = j + 1
    End If
  Wend

MashEnd:

'<MASH> ---------------------------------------------------------i level
' <NAME>Single Infusion, Full Body</NAME>------------------------j level
' <VERSION>1</VERSION>
' <GRAIN_TEMP>22.22222200</GRAIN_TEMP>
' <TUN_TEMP>22.22222200</TUN_TEMP>
' <SPARGE_TEMP>75.55555600</SPARGE_TEMP>
' <PH>5.4</PH>
' <TUN_WEIGHT>1.81436800</TUN_WEIGHT>
' <TUN_SPECIFIC_HEAT>0.30000000</TUN_SPECIFIC_HEAT>
' <EQUIP_ADJUST>FALSE</EQUIP_ADJUST>
' <NOTES></NOTES>
' <DISPLAY_GRAIN_TEMP>72.0 F</DISPLAY_GRAIN_TEMP>
' <DISPLAY_TUN_TEMP>72.0</DISPLAY_TUN_TEMP>
' <DISPLAY_SPARGE_TEMP>168.0 F</DISPLAY_SPARGE_TEMP>
' <DISPLAY_TUN_WEIGHT>4.00 lb</DISPLAY_TUN_WEIGHT>
'<MASH_STEPS>--------------------------------------------------still j level
'<MASH_STEP>-------------------------------------------------------l level
' <NAME>Mash In</NAME>----------------------------------------------k level
' <VERSION>1</VERSION>
' <TYPE>Infusion</TYPE>
' <INFUSE_AMOUNT>10.646532</INFUSE_AMOUNT>
' <STEP_TIME>45</STEP_TIME>
' <STEP_TEMP>70.00000000</STEP_TEMP>
' <RAMP_TIME>2</RAMP_TIME>
' <END_TEMP>70.00000000</END_TEMP>
' <DESCRIPTION>Add 11.25 qt of water at 170.5 F</DESCRIPTION>
' <WATER_GRAIN_RATIO>1.25</WATER_GRAIN_RATIO>
' <DECOCTION_AMT>0.00 qt</DECOCTION_AMT>
' <INFUSE_TEMP>170.5 F</INFUSE_TEMP>
' <DISPLAY_STEP_TEMP>DISPLAY_STEP_TEMP</DISPLAY_STEP_TEMP>
' <DISPLAY_INFUSE_AMT>11.25 qt</DISPLAY_INFUSE_AMT>
'</MASH_STEP>
'<MASH_STEP>
' <NAME>Mash Out</NAME>
' <VERSION>1</VERSION>
' <TYPE>Infusion</TYPE>
' <INFUSE_AMOUNT>6.813780</INFUSE_AMOUNT>
' <STEP_TIME>10</STEP_TIME>
' <STEP_TEMP>75.55555600</STEP_TEMP>
' <RAMP_TIME>2</RAMP_TIME>
' <END_TEMP>75.55555600</END_TEMP>
' <DESCRIPTION>Add 7.20 qt of water at 185.9 F</DESCRIPTION>
' <WATER_GRAIN_RATIO>2.05</WATER_GRAIN_RATIO>
' <DECOCTION_AMT>0.00 qt</DECOCTION_AMT>
' <INFUSE_TEMP>185.9 F</INFUSE_TEMP>
' <DISPLAY_STEP_TEMP>DISPLAY_STEP_TEMP</DISPLAY_STEP_TEMP>
' <DISPLAY_INFUSE_AMT>7.20 qt</DISPLAY_INFUSE_AMT>
'</MASH_STEP>
'</MASH_STEPS>
'</MASH>

  End If
  
  
  'get/assign hops *** DONE
  If root.ChildNodes(i).tagName = "HOPS" Then
  j = 0
  k = 0
  Dim HopRow As Integer
  Dim HBU As Double
  Dim SearchRow As Integer
  Dim HaveAlpha As Double
  Dim HaveAmount As Double
  HopRow = 38
  SearchRow = 3
  While (j < root.ChildNodes(i).ChildNodes.Length) And (HopRow < 48) ' number of hops
    HaveAlpha = 0
    HaveAmount = 0
    While k < root.ChildNodes(i).ChildNodes(j).ChildNodes.Length 'hop properties
      If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "NAME" Then
        'Do we have this Hop already?
        While (root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text <> Worksheets(4).Range("A" & SearchRow)) And (Worksheets(4).Cells(SearchRow, 1) <> "END")
          SearchRow = SearchRow + 1
          If Worksheets(4).Range("A" & SearchRow) = "END" Then
            MsgBox "The hop: " & root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text & " isn't in the database. Please enter manually."
          End If
        Wend
        Range("D" & HopRow) = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
      End If
      
      If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "AMOUNT" Then
        Range("E" & HopRow) = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text * 1000 'kg
      End If
      
      If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "ALPHA" Then
        Worksheets(4).Range("D" & SearchRow) = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
      End If
      
      If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "USE" Then
        Range("F" & HopRow) = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
      End If
      
      If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "TIME" Then
        If Range("F" & HopRow).Text = "Dry Hop" Then
            Range("C" & HopRow) = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text / 1440
        Else
            Range("C" & HopRow) = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
        End If
      End If
      k = k + 1
    Wend
    'Move on to the next hop
    HopRow = HopRow + 1
    j = j + 1
    k = 0
  Wend
  
  
  
  '<HOP>
    '<NAME>Tettnanger (German)</NAME>
    '<VERSION>1</VERSION>
    '<ALPHA>0.045</ALPHA>
    '<AMOUNT>14.17475</AMOUNT>
    '<USE>Boil</USE>
    '<TIME>60</TIME>
    '<DISPLAY_AMOUNT>0.5 oz</DISPLAY_AMOUNT>
  '</HOP>
  '<HOP>
    '<NAME>Tettnanger (German)</NAME>
    '<VERSION>1</VERSION>
    '<ALPHA>0.045</ALPHA>
    '<AMOUNT>28.3495</AMOUNT>
    '<USE>Boil</USE>
    '<TIME>10</TIME>
    '<DISPLAY_AMOUNT>1 oz</DISPLAY_AMOUNT>
  '</HOP>
  '<HOP>
    '<NAME>Tettnanger (German)</NAME>
    '<VERSION>1</VERSION>
    '<ALPHA>0.045</ALPHA>
    '<AMOUNT>14.17475</AMOUNT>
    '<USE>Boil</USE>
    '<TIME>5</TIME>
    '<DISPLAY_AMOUNT>0.5 oz</DISPLAY_AMOUNT>
  '</HOP>
  End If
  
  
  
  If root.ChildNodes(i).tagName = "FERMENTABLES" Then
  'get/assign fermentables *** DONE
  j = 0
  k = 0
  Dim MaltRow As Integer
  MaltRow = 25
  SearchRow = 5
  Dim kgs As Double
  While (j < root.ChildNodes(i).ChildNodes.Length) And (MaltRow < 36) ' number of Malts
    While k < root.ChildNodes(i).ChildNodes(j).ChildNodes.Length 'Malt properties
      If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "NAME" Then
        'Do we have this Malt already?
        While (root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text <> Worksheets(3).Range("C" & SearchRow)) And (Worksheets(3).Cells(SearchRow, 1) <> "END")
          SearchRow = SearchRow + 1
          If Worksheets(3).Range("A" & SearchRow) = "END" Then
            MsgBox "The malt:" & root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text & " may not be in the database. Please enter manually."
          End If
        Wend
        Range("D" & MaltRow) = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
      End If
      
      If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "AMOUNT" Then
      kgs = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
      Range("C" & MaltRow) = Round(kgs, 2)
      End If
      k = k + 1
    Wend
    'Move on to the next Malt
    MaltRow = MaltRow + 1
    j = j + 1
    k = 0
  Wend
  '<FERMENTABLE>
  '<NAME>Pilsner (2 Row) UK</NAME>
  '<VERSION>1</VERSION>
  '<TYPE>Grain</TYPE>
  '<AMOUNT>3.86363636363636</AMOUNT>
  '<YIELD>1.036</YIELD>
  '<COLOR>1</COLOR>
  '<ORIGIN>#N/A</ORIGIN>
  '</FERMENTABLE>
  End If
  
  'get/assign yeast
  If root.ChildNodes(i).tagName = "YEASTS" Then
  j = 0
  k = 0
  'if there is no yeast
  If root.ChildNodes(i).ChildNodes.Length = 0 Then
    GoTo Nah
  End If
  SearchRow = 2
  While k < root.ChildNodes(i).ChildNodes(j).ChildNodes.Length 'Yeast properties
    If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "PRODUCT_ID" Then
      If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text = "" Then
        MsgBox "No yeast detected by Product ID. Use the Yeast Tab to find the ID you're looking for."
        Range("C57") = 374
      Else
        'Do we have this Yeast already?
        While (root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text <> Worksheets(5).Range("D" & SearchRow)) And (SearchRow < 457)
          If SearchRow = 457 Then
            MsgBox "The Yeast:" & root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text & " may be in the database. Use the yeast tab to find the ID."
          End If
          SearchRow = SearchRow + 1
        Wend
        If SearchRow <> 457 Then
          Range("G51") = Worksheets(5).Range("C" & SearchRow)
          Range("H51") = Worksheets(5).Range("B" & SearchRow)
        Else
          Range("G51") = Worksheets(5).Range("B" & 375)
          Range("H51") = Worksheets(5).Range("C" & 375)
        End If
      End If
    End If
    k = k + 1
  Wend

  '<YEAST>
  '<NAME>Saflager - German Lager Yeast </NAME>
  '<VERSION>1</VERSION>
  '<TYPE>Lager</TYPE>
  '<FORM>Dry</FORM>
  '<AMOUNT>1</AMOUNT>
  '<LABORATORY>Fermentis / Safale</LABORATORY>
  '<PRODUCT_ID>W-34/70</PRODUCT_ID>
  '<MIN_TEMPERATURE>48</MIN_TEMPERATURE>
  '<MAX_TEMPERATURE>72</MAX_TEMPERATURE>
  '<FLOCCULATION>High</FLOCCULATION>
  '<ATTENUATION>83</ATTENUATION>
  '</YEAST>
  End If
  
  
    'get/assign water *** DONE
    If root.ChildNodes(i).tagName = "WATERS" Then
    k = 0
    While k < root.ChildNodes(i).ChildNodes(j).ChildNodes.Length 'Yeast properties
        If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "CALCIUM" Then
            Worksheets(6).Range("B6") = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
        End If
        If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "BICARBONATE" Then
            Worksheets(6).Range("G6") = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
        End If
        If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "SULFATE" Then
            Worksheets(6).Range("D6") = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
        End If
        If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "CHLORIDE" Then
            Worksheets(6).Range("F6") = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
        End If
        If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "SODIUM" Then
            Worksheets(6).Range("E6") = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
        End If
        If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "MAGNESIUM" Then
            Worksheets(6).Range("C6") = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
        End If
        k = k + 1
    Wend
    
    '<WATER>
    '<NAME>Balanced/Modified</NAME>
    '<VERSION>1</VERSION>
    '<AMOUNT>29.549585</AMOUNT>
    '<CALCIUM>90</CALCIUM>
    '<BICARBONATE>100</BICARBONATE>
    '<SULFATE>60</SULFATE>
    '<CHLORIDE>95</CHLORIDE>
    '<SODIUM>25</SODIUM>
    '<MAGNESIUM>5</MAGNESIUM>
    '</WATER>
    End If
    
    If root.ChildNodes(i).tagName = "MISCS" Then
    j = 0 'number of adjuncts
    While (j < root.ChildNodes(i).ChildNodes.Length) And (51 + j < 55)
    k = 0 'properties
        While k < root.ChildNodes(i).ChildNodes(j).ChildNodes.Length 'properties
            If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "NAME" Then
                Range("D" & 51 + j) = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
            End If
            If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "AMOUNT" Then
                Range("C" & 51 + j) = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
            End If
            If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).tagName = "TIME" Then
                If root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text < 1439 Then
                    Range("E" & 51 + j) = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text
                Else
                    Range("E" & 51 + j) = root.ChildNodes(i).ChildNodes(j).ChildNodes(k).Text / 1440 & " day(s)"
                End If
            End If
            k = k + 1
        Wend
    j = j + 1
    Wend
    End If

'<MISCS> ----------- i
    '<MISC>---------------j
        '<NAME>Irish Moss</NAME>-----------------k
        '<VERSION>1</VERSION>
        '<TYPE>Fining</TYPE>
        '<USE>Boil</USE>
        '<AMOUNT>0.001232</AMOUNT>
        '<TIME>10.000</TIME>
        '<AMOUNT_IS_WEIGHT>FALSE</AMOUNT_IS_WEIGHT>
        '<USE_FOR>Clarity</USE_FOR>
        '<NOTES>
        'Fining agent that aids in the post-boil protein break. Reduces protein chill haze and improves beer clarity.
        '</NOTES>
        '<DISPLAY_AMOUNT>0.25 tsp</DISPLAY_AMOUNT>
        '<INVENTORY>0.00 tsp</INVENTORY>
        '<DISPLAY_TIME>10.0 min</DISPLAY_TIME>
        '<BATCH_SIZE>5.00 gal</BATCH_SIZE>
    '</MISC>
    '<MISC>
        '<NAME>Polyclar</NAME>
        '<VERSION>1</VERSION>
        '<TYPE>Fining</TYPE>
        '<USE>Secondary</USE>
        '<AMOUNT>0.007393</AMOUNT>
        '<TIME>1440.000</TIME>
        '<AMOUNT_IS_WEIGHT>FALSE</AMOUNT_IS_WEIGHT>
        '<USE_FOR>Chill Haze</USE_FOR>
        '<NOTES>
        'Plastic powder that reduces chill haze by removing tannins and proteins. Add to secondary after yeast has settled. Amounts vary by manufacturer -- check instructions before adding. Do not boil.
        '</NOTES>
        '<DISPLAY_AMOUNT>0.25 oz</DISPLAY_AMOUNT>
        '<INVENTORY>0.00 oz</INVENTORY>
        '<DISPLAY_TIME>1.0 days</DISPLAY_TIME>
        '<BATCH_SIZE>5.00 gal</BATCH_SIZE>
    '</MISC>
'</MISCS>


Nah:
    
  'Increment one
  i = i + 1
Wend


TheEnd:


'Let the metric side update the english side again
Worksheets(1).Range("A1").ClearContents

'actually update
Worksheets(7).Convert_to_Eng

'Go back to sheet you triggered macro from
Worksheets(sheetNo).Activate

End Sub



"""
