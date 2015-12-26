# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	pango

Summary:	Ruby binding of Pango
Name:		rubygem-%{rbname}

Version:	3.0.7
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:  rubygem(glib2)
BuildRequires:  rubygem-glib2-devel
BuildRequires:	rubygem(cairo)
BuildRequires:	rubygem-cairo-devel
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
Obsoletes:      ruby-pango

%description
Ruby binding of Pango

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%package    devel                                                                                                                                                                                              
Summary:    Development files for %{name}
Group:      Development/Ruby

%description	devel
Development files for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_sitearchdir}/%{rbname}.so

%files doc
%doc %{gem_dir}/doc/%{rbname}-%{version}

%files devel
%{ruby_sitearchdir}/*.h


%changelog

