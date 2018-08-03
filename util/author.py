import pandas as pd

def results2csv(index_data, prediction_data, file_name):
	"""
	Persist Prediction Results data to CSV file, for the CSV  file to be submitted to Kaggle
	"""
	df = pd.DataFrame({
		# test_x.index.name : test_x.index,
		# 'Survived' : test_y_pred
		'PassengerId' : index_data,
		'Survived' : prediction_data
    })
	df.set_index('PassengerId', inplace=True)
	df.to_csv(file_name)