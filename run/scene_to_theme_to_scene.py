import keyword_to_theme as run
import os
from collections import defaultdict
import csv



upper_dir = os.path.dirname(os.getcwd())

data_dir = os.path.join(upper_dir, 'data')
filename = os.path.join(data_dir, 'Scene.csv')


def load_data():
    """
    This method reads the dataset, and returns a list of rows.
    Each row is a list containing the values in each column.
    """    
    with open(filename, 'rb') as f:
        f.seek(0)
        reader = csv.reader(f)
        return [l for l in reader]


def build_SceneToTheme_map():
	result = []
	SceneThemeCollect = defaultdict(list)
	SceneThemeCount = dict()
	for row in Scene:
	    # print "Movie Name: " + row[0]
	    for i in xrange(1, len(row)):
	        if row[i] == None or row[i] == "":
	            break
	        result = run.get_theme(row[i])[0]
	        SceneThemeCollect[result[0].encode("ascii")].append(row[0].encode("ascii") + "/Scene" + str(i))
	        SceneThemeCollect[result[1].encode("ascii")].append(row[0].encode("ascii") + "/Scene" + str(i))
	        
	        SceneThemeCount[result[0]] = SceneThemeCount.get(result[0], 0) + 1
	        SceneThemeCount[result[1]] = SceneThemeCount.get(result[1], 0) + 1
	return  SceneThemeCollect      


Scene = load_data()
SceneThemeCollect = build_SceneToTheme_map()

# demo: example with Kill the Messenger (2014)/Scene1
print "Clicked Theme: Kill the Messenger (2014)/Scene1"
test = run.get_theme("['ensemble of people', 'boxing (light heavyweight)', 'people', 'hotel setting', 'brasserie', 'surgical instrument', 'sprinkler', 'reading lamp', 'discussion', 'actor', 'heavyweight wrestler', 'knife', 'woman', 'hairdresser', 'cannon', 'bandage', 'laboratory coat', 'elegant hotel', 'coiffeur (hairdresser)', 'bodyguard', 'naval gun', 'waiter', 'physical therapist', 'support column']")

for i in xrange(2):
    for j in xrange(len(SceneThemeCollect[test[0][i]])):
        if SceneThemeCollect[test[0][i]][j] == 'Kill the Messenger (2014)/Scene1':
            continue
        else: 
        	print test[0][i]
        	print "Recommended Theme: " + SceneThemeCollect[test[0][i]][j]


# demo: example with Kill the Messenger (2014)/Scene1
print "\nClicked Theme: Grandma's Boy (2006)/Scene2"
test = run.get_theme("['television reporter', 'platinum blond', 'family', 'people', 'religion related', 'computer user', 'sibling', 'barmaid', 'big sister', 'sociologist', 'art gallery', 'newsreader', 'grandmother', 'great-aunt', 'mug', 'lecturer', 'woman', 'hairdresser', 'headwaiter', 'grandmother (nan)', 'call center', 'magician', 'teacher', 'waiter', 'broadcasting', 'reception']")

for i in xrange(2):
    for j in xrange(len(SceneThemeCollect[test[0][i]])):
        if SceneThemeCollect[test[0][i]][j] == "Grandma's Boy (2006)/Scene2":
            continue
        else:
      		print test[0][i]
        	print "Recommended Theme: " + SceneThemeCollect[test[0][i]][j]


