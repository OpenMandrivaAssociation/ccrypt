Name: ccrypt
Version: 1.10
Release: 2
Source0: http://ccrypt.sourceforge.net/download/%{name}-%{version}.tar.gz
Summary: Utility for encrypting and decrypting files and streams
URL: http://ccrypt.sf.net/
License: GPL
Group: File tools
BuildRequires:	emacs

%description
ccrypt is a utility for encrypting and decrypting files and streams. It was
designed as a replacement for the standard unix crypt utility, which is
notorious for using a very weak encryption algorithm. ccrypt is based on
the Rijndael block cipher, a version of which is also used in the Advanced
Encryption Standard (AES).
This cipher is believed to provide very strong security.

Unlike unix crypt, the algorithm provided by ccrypt is not symmetric, i.e.,
one must specify whether to encrypt or decrypt. The most common way to
invoke ccrypt is via the commands ccencrypt and ccdecrypt. There is also
a ccat command for decrypting a file directly to the terminal, thus
reducing the likelihood of leaving temporary plaintext files around.

In addition, there is a compatibility mode for decrypting legacy unix
crypt files. An emacs mode is also supplied for editing encrypted
text files.

Encryption and decryption depends on a keyword (or key phrase) supplied
by the user. By default, the user is prompted to enter a keyword from
the terminal. Keywords can consist of any number of characters, and
all characters are significant (although ccrypt internally hashes the
key to 256 bits). Longer keywords provide better security than short
ones, since they are less likely to be discovered by exhaustive search.

%package emacs
Summary: Emacs mode for editing files encrypted with ccrypt
Group: File tools
Requires: %{name} = %{EVRD}

%description emacs
Emacs mode for editing files encrypted with ccrypt

%prep
%setup -q
%configure

%build
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{_mandir}/*/*

%files emacs
%{_datadir}/emacs/site-lisp/*
