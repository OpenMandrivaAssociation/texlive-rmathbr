%global tl_name rmathbr
%global tl_revision 57173

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.1
Release:	%{tl_revision}.1
Summary:	Repeating of math operator at the broken line and the new line in inline equa...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rmathbr
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rmathbr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rmathbr.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rmathbr.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Repeating of math operators at the broken line and the new line in
inline equations is used in Cyrillic mathematical typography (Russian
for example), but unfortunately LaTeX does not provide such an option.
This package solves the problem by extending ideas described in M. I.
Grinchuk "TeX and Russian Traditions of Typesetting", TUGboat 17(4)
(1996) 385 and supports most of LaTeX mathematical packages. See the
documentation for details.

