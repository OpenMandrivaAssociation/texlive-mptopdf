Name:		texlive-mptopdf
Version:	20111102
Release:	1
Summary:	mpost to PDF, native MetaPost graphics inclusion
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mptopdf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mptopdf.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-mptopdf.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The mptopdf script does standalone conversion from mpost to
PDF, using the supp-* and syst-* files.  They also allow native
MetaPost graphics inclusion in LaTeX (via pdftex.def) and
ConTeXt.  They can be used independently of the rest of
ConTeXt, yet are maintained as part of it.  So in TeX Live we
pull them out to this separate package for the benefit of LaTeX
users who do not install the rest of ConTeXt.  This can be
found on CTAN in macros/pdftex/graphics.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/mptopdf
%{_texmfdistdir}/scripts/context/perl/mptopdf.pl
%{_texmfdistdir}/tex/context/base/supp-mis.mkii
%{_texmfdistdir}/tex/context/base/supp-mpe.mkii
%{_texmfdistdir}/tex/context/base/supp-pdf.mkii
%{_texmfdistdir}/tex/context/base/syst-tex.mkii
%{_texmfdistdir}/tex/generic/context/mptopdf.tex
%doc %{_mandir}/man1/mptopdf.1*
%doc %{_texmfdir}/doc/man/man1/mptopdf.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/context/perl/mptopdf.pl mptopdf
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
