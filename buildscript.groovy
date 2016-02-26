import org.jenkinsci.plugins.ghprb.*


def repoURL = 'https://github.com/freshbooks/ebs-snapshots'

job('infrastructure+ebs-snapshots') {
    label('docker')
    concurrentBuild()
    properties {
        propertiesNodes << new NodeBuilder().'com.coravy.hudson.plugins.github.GithubProjectProperty' {
            delegate.projectUrl(repoURL)
        }
    }
    scm {
        git{
            remote {
                name('origin')
                url(repoURL+'.git')
            }
            branches('*/master')
        }
    }
    triggers {
        scm('H 2 * * *')
    }
    steps {
        shell('make snapshots')
    }
}
