# Create file using Puppet

file {'/tmp/school':
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
}
