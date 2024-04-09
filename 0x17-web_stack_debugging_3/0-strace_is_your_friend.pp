# Creat a manifest that fix all termintion of php.

exec { 'fix_php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin/', '/usr/loca/bin/'],
}
