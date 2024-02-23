# install a package 
exec { 'install_flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
    path    => ['/usr/bin', '/usr/local/bin'],
    unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}