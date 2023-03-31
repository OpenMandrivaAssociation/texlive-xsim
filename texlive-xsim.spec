Name:		texlive-xsim
Version:	61988
Release:	2
Summary:	eXercise Sheets IMproved
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xsim
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xsim.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xsim.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package helps in creating exercises and the corresponding
solutions. It is the official successor of the exsheets package
and fixes/improves various long-standing issues.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/xsim
%doc %{_texmfdistdir}/doc/latex/xsim

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
