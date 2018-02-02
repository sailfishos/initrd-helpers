Name:       initrd-helpers
Summary:    Helper scripts and tools for init ramdisks
Version:    0.0.1
Release:    1
Group:      System/Boot
License:    GPLv2
Source0:    %{name}-%{version}.tar.gz

Requires:  btrfs-progs
Requires:  e2fsprogs
Requires:  pigz

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}


%build

%install
mkdir -p %{buildroot}/sbin/
install -D -m 755 btrfs-mount-repair %{buildroot}/sbin/btrfs-mount-repair
install -D -m 755 factory-reset-external %{buildroot}/sbin/factory-reset-external
install -D -m 755 factory-reset-lvm %{buildroot}/sbin/factory-reset-lvm
install -D -m 755 find-mmc-bypartlabel %{buildroot}/sbin/find-mmc-bypartlabel

%files
%defattr(-,root,root,-)
/sbin/btrfs-mount-repair
/sbin/factory-reset-external
/sbin/factory-reset-lvm
/sbin/find-mmc-bypartlabel

%doc LICENSE README



