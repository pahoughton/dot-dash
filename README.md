## dash-dot

Operations monitoring and response system.

Green dot - life is good - low priority tickets
...       - plenty to do - 1|0 high priority tickets
Red dot   - Dash'ing     - 2+ high priority tickets

## Status

POC iterations

[![Test Build Status](https://travis-ci.org/pahoughton/dot-dash.png)](https://travis-ci.org/pahoughton/dot-dash)



## Dependencies

	$ [ -e yum ] && sudo yum install ansible
	$ [ -e apt ] && sudo apt install ansible

	$ git clone https://github.com/pahoughton/dot-dash
	$ cd dash-dot
	$ sudo ansible-playbook -p site-depends.yml

## Validation

	rake test
    $ do grep ':[0-9]+ molecule test' test/rake.test.runtimes.txt ; done
    # echo for test run times
    $ do tail -f test/rake.test.runtimes.txt ; done
    # echo to watch progress

## Features

- Monitoring system
- Alerting system
- Open Source

### Monitoring

- response times
- resource utilization
- applications
- hardware

### Alerting

- auto ticket generation
- ticket creation drives notification (sms/email)
- tickets updated by ci workflows


## Use Cases

Retention: save everything forever - iterate data driven automation

from an engineers perspective ...

What changed? Unanticipated load? material or communications failure?

Most common answer will be an unanticipated use case, hence no
validation of the automated responce to the event.

Provide complete relative details for imperfections with responce time
relative to age and utilization.

Single entry point (url) for application, system and hardware status
with built in research paths.

Ties user activity to hardware performance.

UI First url is the dot which a visual artist will be able to provide a
quick view with details becomeing more obvious the more you look (ok a
BIG CIRCLE, not a dot :).

The dash is what happens next. Respond to the dot and it provides the
path to more detail relative to who you are.

as the images provide the research path and ongoing status, the are
watching your progress, time to action, actions taken through
closure.  We live we Learn :). When everyone's responce to the dot is
to smile and stop looking, we get to play with then next toy

Every imperfection generates and assigns a ticket. closed tickets
include automation potential.

## Notes

Monitoring and Ticketing UI will be plenty. Tickets are monitored and
both are fed from the same hands. Tickets provide notification,
tracking and knowledge base. The monitor will have relevant ticket
summaries.

when the dot is not pretty, you dash off too learn why and what you
can do to beautify the dot.

end game? elimination of repetition through iterative validation
(D.R.Y.).




## Tools (FIXME LINKS)

monitoring:
  Prometheus node exporter
  Telegraf
  syslog
  LogStash
  Metricbeat

alerting:
  ElasticSearch(ELK)
    open source
    designed for long term storage
  Prometheus
	open source
    15 day retention w/o easy long term storage
    https://prometheus.io/docs/alerting/overview/
    https://www.robustperception.io/scaling-and-federating-prometheus/

Graphs:  Grafana

ticket:
    jira
		has api
		has alerting interfaces (ELK & Prometheus)
	bugzilla - loosing popularity to phabricator
	phabricator
	   has api
	   does not have interface w/ alerting tools
	   https://secure.phabricator.com/book/phabricator/article/installation_guide/
	openproject https://github.com/opf/openproject

Validation:
	ci - zuul
	serverspec - testinfra, rspec-serverspec
	ansible - molecule
	python - tox, pytest, pytest-spec
	ruby - rspec

Repo Managers
	yum
	apt
	pip
	gem
	cpan
	git


## Install

./install

## Usage

url

## Contribute

validated pull request will be reviewed and merged.

[Github pahoughton/dot-dash](https://github.com/pahoughton/dot-dash)

## Licenses

2018-09-05 (cc) <paul4hough@gmail.com>

[![LICENSE](http://i.creativecommons.org/l/by/3.0/88x31.png)](http://creativecommons.org/licenses/by/3.0/)

[![endorse](https://api.coderwall.com/pahoughton/endorsecount.png)](https://coderwall.com/pahoughton)
