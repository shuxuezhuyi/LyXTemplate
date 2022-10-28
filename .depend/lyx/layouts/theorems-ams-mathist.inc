# Original Author : David L. Johnson <dlj0@lehigh.edu>
# Probably broken by Jean-Marc Lasgouttes <Jean-Marc.Lasgouttes@inria.fr>
# modified and modularized by Emmanuel GUREGHIAN <gureghia@boston.bertin.fr>
# Tinkered with Sep. '07 by Paul Rubin <rubin@msu.edu>
# Modularized Jan 08 by Richard Heck <rgheck@comcast.net>
# modified by mathist

# The environments defined are :
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

Style Theorem
	Category              Reasoning
	Margin                First_Dynamic
	LatexType             Environment
	LatexName             Theorem
	NextNoIndent          1
	ResetArgs             1
	Argument 1
		LabelString    "Optional Parameter"
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
	LabelCounter          theorem
	LabelString           "Theorem \thetheorem"
	Font
	  Family              Typewriter
	EndFont
	LabelFont
	  Series              Bold
	EndFont
	Requires              amsthm
End


Style Corollary
	CopyStyle             Theorem
	DependsOn	      Theorem
	LatexName             Corollary
	LabelString           "Corollary \thetheorem"
End


Style Lemma
	CopyStyle             Theorem
	DependsOn	      Theorem
	LatexName             Lemma
	LabelString           "Lemma \thetheorem"
End


Style Proposition
	CopyStyle             Theorem
	DependsOn	      Theorem
	LatexName             Proposition
	LabelString           "Proposition \thetheorem"
End


Style Conjecture
	CopyStyle             Theorem
	DependsOn	      Theorem
	LatexName             Conjecture
	LabelString           "Conjecture \thetheorem"
End


Style Fact
	CopyStyle             Theorem
	DependsOn	      Theorem
	LatexName             Fact
	LabelString           "Fact \thetheorem"
End


Style Definition
	CopyStyle             Theorem
	DependsOn	      Theorem
	LatexName             Definition
	LabelString           "Definition \thetheorem"
End


Style Example
	CopyStyle             Definition
	DependsOn	      Theorem
	LatexName             Example
	LabelString           "Example \thetheorem"
End


Style Problem
	CopyStyle             Definition
	DependsOn	      Theorem
	LatexName             Problem
	LabelString           "Problem \thetheorem"
End


Style Exercise
	CopyStyle             Definition
	DependsOn	      Theorem
	LatexName             Exercise
	LabelString           "Exercise \thetheorem"
End


Style Remark
	CopyStyle             Theorem
	DependsOn	      Theorem
	LatexName             Note
	LabelString           "Remark \thetheorem"
	LabelFont
	  Shape               Italic
	EndFont
End


Style Claim
	CopyStyle             Remark
	DependsOn	      Theorem
	LatexName             Claim
	LabelString           "Claim \thetheorem"
End

Input theorems-refprefix-mathist.inc
