file { '/var/www/html/wp-content/uploads':
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

service { 'apache2':
  ensure => 'running',
  enable => true,
}

