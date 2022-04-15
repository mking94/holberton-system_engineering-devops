# Run command

exec { 'exec':
    command => 'pkill killmeknow',
    path    => '/usr/local/bin/:/bin/',
  }
