# Author : mathist <mathist@139.com>

Format 66

Provides stdinsets 1

InsetLayout Flex:ProofAsInset
   LyXType     custom
   LatexName   Proof
   LatexType   Environment
   Decoration  classic
   Argument 1
     LabelString         "Proof Name"
   EndArgument
   BgColor background
   MultiPar    true
   LabelString Proof
End

InsetLayout Flex:HINTAsInset
   CopyStyle   Flex:ProofAsInset
   LatexName   HINT
   LabelString HINT
End
