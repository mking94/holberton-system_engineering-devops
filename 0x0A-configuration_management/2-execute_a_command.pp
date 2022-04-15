# Run command

exec { 'pkill':
    command => 'pkill killmeknow',
    path    => '/usr/local/bin/:/bin/',
  }
