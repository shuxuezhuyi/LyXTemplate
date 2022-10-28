# Author : David L. Johnson <dlj0@lehigh.edu>
# Probably broken by Jean-Marc Lasgouttes <Jean-Marc.Lasgouttes@inria.fr>
# modified and modularized by Emmanuel GUREGHIAN <gureghia@boston.bertin.fr>
# This version has Theorems and other results numbered in one sequence, and all
# numbered environments (figures as well) containing the section number.
# (Themorem (1.1), Corollary (1.2) Theorem (1.3), etc.
# These are only the theorems styles environnements
# Tinkered with Sep. '07 by Paul Rubin <rubin@msu.edu>
# Modularized Jan 08 by Richard Heck <rgheck@comcast.net>
# modified by mathist <mathist@139.com>

Format 66

Style Proof
	Category              DoNotUse
	Margin                First_Dynamic
	LatexType             Environment
	LatexName             Proof
	NextNoIndent          1
	ResetArgs             1
	Argument 1
		LabelString   "Name"
		Tooltip       "Alternative proof string"
	EndArgument
	LabelSep              xx
	ParIndent             MMM
	ParSkip               0.4
	ItemSep               0.2
	TopSep                0.7
	BottomSep             0.7
	ParSep                0.3
	Align                 Block
	AlignPossible         Block, Left
	LabelType             Static
	LabelString           "Proof."
	EndLabelType          Box
	LabelFont
	  Series               Bold
	EndFont
End


Style HINT
	CopyStyle             Proof
	LatexName             HINT
	LabelString           "HINT."
End

