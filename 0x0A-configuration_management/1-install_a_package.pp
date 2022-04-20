# Install package puppet-lint.

pip::install { 'flask':
  ensure  => present,
  version => '2.1.0',
  package => 'flask',
}
