# Create file using Puppet

  file { 'holbertonschool': 
    ensure => 'present',
    content => 'I love Puppet', 
    owner => 'www-data',
    group => 'www-data',
    mode => '0744',
    path => '/tmp/school'
  }
