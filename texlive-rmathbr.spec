Name:		texlive-rmathbr
Version:	57173
Release:	2
Summary:	Repeating of math operator at the broken line and the new line in inline equations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rmathbr
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rmathbr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rmathbr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rmathbr.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Repeating of math operators at the broken line and the new line
in inline equations is used in Cyrillic mathematical typography
(Russian for example), but unfortunately LaTeX does not provide
such an option. This package solves the problem by extending
ideas described in M. I. Grinchuk "TeX and Russian Traditions
of Typesetting", TUGboat 17(4) (1996) 385 and supports most of
LaTeX mathematical packages. See the documentation for details.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/rmathbr
%{_texmfdistdir}/tex/latex/rmathbr
%doc %{_texmfdistdir}/doc/latex/rmathbr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
