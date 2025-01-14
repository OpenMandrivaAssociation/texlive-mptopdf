Name:		texlive-mptopdf
Version:	61520
Release:	2
Summary:	mpost to PDF, native MetaPost graphics inclusion
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mptopdf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mptopdf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Provides:	texlive-mptopdf.bin = %{EVRD}

%description
The mptopdf script does standalone conversion from mpost to
PDF, using the supp-* and syst-* files.  They also allow native
MetaPost graphics inclusion in LaTeX (via pdftex.def) and
ConTeXt.  They can be used independently of the rest of
ConTeXt, yet are maintained as part of it.  So in TeX Live we
pull them out to this separate package for the benefit of LaTeX
users who do not install the rest of ConTeXt.  This can be
found on CTAN in macros/pdftex/graphics.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/mptopdf
%{_texmfdistdir}/scripts/context/perl/mptopdf.pl
%{_texmfdistdir}/scripts/context/stubs/mswin/mptopdf.exe
%{_texmfdistdir}/tex/context/base/mkii
%{_texmfdistdir}/tex/generic/context/mptopdf
%_texmf_fmtutil_d/mptopdf
%doc %{_texmfdistdir}/doc/context/scripts/mkii/mptopdf.man
%doc %{_mandir}/man1/mptopdf.1*
%doc %{_texmfdistdir}/doc/man/man1/mptopdf.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/context/perl/mptopdf.pl mptopdf
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/mptopdf <<EOF
#
# from mptopdf:
mptopdf pdftex - -translate-file=cp227.tcx mptopdf.tex
EOF
