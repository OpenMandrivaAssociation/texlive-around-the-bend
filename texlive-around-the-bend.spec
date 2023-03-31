Name:		texlive-around-the-bend
Version:	15878
Release:	2
Summary:	Typeset exercises in TeX, with answers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/challenges/AroBend
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/around-the-bend.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/around-the-bend.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a typeset version of the files of the aro-bend, plus
three extra questions (with their answers) that Michael Downes
didn't manage to get onto CTAN.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/around-the-bend/AroundTheBend.pdf
%doc %{_texmfdistdir}/doc/generic/around-the-bend/AroundTheBend.tex
%doc %{_texmfdistdir}/doc/generic/around-the-bend/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
