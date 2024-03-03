from note_client import Note

EMAIL = ''
PASSWORD = ''
USER_ID = ''

TITLE = 'Sample'
CONTENT_PATH = 'content.txt'
TAG_LIST = ['sample_tag']

# > If an image is specified, the index number is entered; if not, no description is given.
# INDEX = 0

# > True if the article is to be published, False if the article is to be saved as a draft; if not specified, the article is saved as a draft.
# POST_SETTING = True

# > True if the execution screen is not displayed, False if it is displayed, or not displayed if not specified.
# HEADLESS = False

# To specify the above three options, add them to the function arguments.

note = Note(email=EMAIL, password=PASSWORD, user_id=USER_ID)
print(note.create_article(title=TITLE, file_name=CONTENT_PATH, input_tag_list=TAG_LIST, image_index=None))

## If successful(Public).
# {'run':'success','title':'Sample','file_path':'content.txt','tag_list':['sample_tag'],'post_setting':'Public','post_url':'https://note.com/USER_ID/n/abc123'}

## If successful(Draft).
# {'run':'success','title':'Sample','file_path':'content.txt','tag_list':['sample_tag'],'post_setting':'Draft'}

## If unsuccessful.
# 'Required data is missing.'