# 2018-10-14 (cc) <paul4hough@gmail.com>
#

$runstart = Time.now

at_exit {
  runtime = Time.at(Time.now - $runstart).utc.strftime("%H:%M:%S.%3N")
  puts "run time: #{runtime}"
}

task :default do
  sh 'rake --tasks'
  exit 1
end

task :ansible_syntax do |task, args|
  sh "ansible-playbook --syntax-check --list-tasks site.yml -i cbed,"
end

task :provision do |task, args|
  sh "vagrant provision"
end

task :vup do |task, args|
  sh "vagrant up"
end
