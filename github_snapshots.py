import boto.ec2
import os
from dateutil import parser
from datetime import timedelta, datetime


class GithubSnapshot(object):

    def __init__(self):
	self.aws_region = os.getenv('AWS_REGION', 'us-east-1')
	self.aws_key = os.getenv('AWS_ACCESS_KEY_ID')
	self.aws_secret = os.getenv('AWS_SECRET_ACCESS_KEY')
	auth = {
	    "aws_access_key_id": self.aws_key,
	    "aws_secret_access_key": self.aws_secret,
	}
	self.ec2 = boto.ec2.connect_to_region(self.aws_region, **auth)
	self.older_than_days = int(os.getenv('SNAPSHOTS_OLDER_THAN_DAYS', 5))

    def find_old_snapshots(self):
	old_snapshot_list = []
	snapshot_filter = {
	    "status": "completed",
	    "tag:expire": "true"
	}
	snapshots = self.ec2.get_all_snapshots(filters=snapshot_filter)
	for snapshot in snapshots:
	    limit = datetime.now() - timedelta(days=self.older_than_days)
	    if parser.parse(snapshot.start_time).date() <= limit.date():
		old_snapshot_list.append(snapshot)
	return old_snapshot_list

    def delete_snapshot(self, snapshot):
	print("Deleting: %s" % snapshot.description)
	self.ec2.delete_snapshot(snapshot.id)

if __name__ == '__main__':
    gh = GithubSnapshot()
    snapshots = gh.find_old_snapshots()
    for snapshot in snapshots:
	gh.delete_snapshot(snapshot)
