# Install package puppet-lint.

pip::install { 'flask':
  package        => 'flask', 
  version        => '2.1.0',
  ensure         => present, 
}
