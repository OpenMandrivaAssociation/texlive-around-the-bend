# revision 15878
# category Package
# catalog-ctan /info/challenges/AroBend
# catalog-date 2009-11-09 13:03:38 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-around-the-bend
Version:	20091109
Release:	1
Summary:	Typeset exercises in TeX, with answers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/challenges/AroBend
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/around-the-bend.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/around-the-bend.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a typeset version of the files of the aro-bend, plus
three extra questions (with their answers) that Michael Downes
didn't manage to get onto CTAN.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/around-the-bend/AroundTheBend.pdf
%doc %{_texmfdistdir}/doc/generic/around-the-bend/AroundTheBend.tex
%doc %{_texmfdistdir}/doc/generic/around-the-bend/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
