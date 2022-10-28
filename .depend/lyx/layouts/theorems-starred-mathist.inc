# Original Author : David L. Johnson <dlj0@lehigh.edu>
# Probably broken by Jean-Marc Lasgouttes <Jean-Marc.Lasgouttes@inria.fr>
# modified and modularized by Emmanuel GUREGHIAN <gureghia@boston.bertin.fr>
# Tinkered with Sep. '07 by Paul Rubin <rubin@msu.edu>
# Modularized Jan 08 by Richard Heck <rgheck@comcast.net>
# modified by mathist

# The starred environnements defined are :
# - Theorem
# - Corollary
# - Lemma
# - Proposition
# - Conjecture
# - Definition
# - Example
# - Problem
# - Exercise
# - Remark
# - Claim
# - Proof

Format 66


Style Theorem*
	Category              Reasoning
	Margin                First_Dynamic
	LatexType             Environment
	LatexName             Theorem*
	NextNoIndent          1
	ResetArgs             1
	Argument 1
		LabelString    "Name"
		Tooltip        "Additional text appended to the theorem header"
	EndArgument
	LabelSep              xx
	ParIndent             MMM
	ParSkip               0.4
	ItemSep               0.2
	TopSep                0.7
	BottomSep             0.7
	ParSep                0.3
	Align                 Block
	AlignPossible         Left
	LabelType             Static
#	LabelCounter          theorem
	LabelString           "Theorem"
	Font
	  Family              Typewriter
	EndFont
	LabelFont
	  Series              Bold
	EndFont
	Requires              amsthm
End


Style Corollary*
	CopyStyle             Theorem*
	LatexName             Corollary*
	LabelString           "Corollary"
End


Style Lemma*
	CopyStyle             Theorem*
	LatexName             Lemma*
	LabelString           "Lemma"
End


Style Proposition*
	CopyStyle             Theorem*
	LatexName             Proposition*
	LabelString           "Proposition"
End


Style Conjecture*
	CopyStyle             Theorem*
	LatexName             Conjecture*
	LabelString           "Conjecture"
End


Style Fact*
	CopyStyle             Theorem*
	LatexName             Fact*
	LabelString           "Fact"
End


Style Definition*
	CopyStyle             Theorem*
	LatexName             Definition*
	LabelString           "Definition"
End


Style Example*
	CopyStyle             Definition*
	LatexName             Example*
	LabelString           "Example"
End


Style Problem*
	CopyStyle             Definition*
	LatexName             Problem*
	LabelString           "Problem"
End


Style Exercise*
	CopyStyle             Definition*
	LatexName             Exercise*
	LabelString           "Exercise"
End


Style Remark*
	CopyStyle             Theorem*
	LatexName             Note*
	LabelString           "Remark"
	LabelFont
	  Shape               Italic
	EndFont
End


Style Claim*
	CopyStyle             Remark*
	LatexName             Claim*
	LabelString           "Claim"
End

