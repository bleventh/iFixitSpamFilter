import requests

# this file will print data into a text file

#if __name__ == "__main__":
# start data gathering here.

class Wiki(object):


   def getWikiObject(self, title):

      response = requests.get('https://www.ifixit.com/api/2.0/wikis/WIKI/%s' % (title))
      attributes = response.json()

      self.can_edit = attributes['can_edit']
      self.documents = attributes['documents']
      self.title = attributes['title']
      self.display_title = attributes['display_title']
      self.revisionid = attributes['revisionid']
      self.namespace = attributes['namespace']
      self.wikiid = attributes['wikiid']
      self.langid = attributes['langid']
      self.contents_raw = attributes['contents_raw']
      self.flags = attributes['flags']
      self.image = attributes['image']
      self.contents_rendered = attributes['contents_rendered']

class User(object):

   # Initialize with userid
   def __init__(self, userid):
      response = requests.get("http://www.ifixit.com/api/2.0/users/%s" \
            % (userid))

      attributes = response.json()

      self.username = attributes['username']
      self.userid = userid
      self.teams = attributes['teams']
      self.reputation = attributes['reputation']
      self.join_date = attributes['join_date']
      self.location = attributes['location']
      self.certification_count = attributes['certification_count']
      self.bronze_badges = attributes['badge_counts']['bronze']
      self.silver_badges = attributes['badge_counts']['silver']
      self.gold_badges = attributes['badge_counts']['gold']
      self.total_badges = attributes['badge_counts']['total']
      self.summary = attributes['summary']
      self.about_raw = attributes['about_raw']
      self.about_rendered = attributes['about_rendered']

class Comment(object):

   def __init__(self, commentId):
      reponse = requests.get("http://www.ifixit.com/api/2.0/comments/%s" \
         % commentId)

      attributes = response.json()

      self.author = attributes['author']
      self.text_raw = attributes['text_raw']
      self.text_rendered = attributes['text_rendered']
      self.rating = attributes['rating']
      self.replies = attributes['replies']

