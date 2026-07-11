%global tl_name mptopdf
%global tl_revision 79616

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	mpost to PDF, native MetaPost graphics inclusion
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/tools/mptopdf
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mptopdf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mptopdf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(mptopdf.bin)
Requires:	texlive(pdftex)
Requires:	texlive(plain)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The mptopdf script does standalone conversion from mpost to PDF, using
the supp-* and syst-* files. They also allow native MetaPost graphics
inclusion in LaTeX (via pdftex.def) and ConTeXt. They can be used
independently of the rest of ConTeXt, yet are maintained as part of it.
So in TeX Live we pull them out to this separate package for the benefit
of LaTeX users who do not install the rest of ConTeXt. This can be found
on CTAN in macros/pdftex/graphics. The files originally come from the
ConTeXt distribution. TL uses the repackaging from
https://github.com/gucci-on-fleek/context-packaging.

