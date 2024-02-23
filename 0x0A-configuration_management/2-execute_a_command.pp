# exxcute a command to stop anthor terminal 

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}