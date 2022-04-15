# Install package using puppet
  package { 'puppet-lint':
    ensure => 'installed',
    version => '2.5.0',
  }
