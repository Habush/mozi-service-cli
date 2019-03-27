## Mozi Service CLI tool

This is a simple command line tool to generate a json file for calling the Moses SingularityNET [Service](https://github.com/Habush/mozi_snet_service)

### Usage

The cli tool requires two paths as input to run the service, the dataset file location and the path to save the output json file.

           #~ mozi-cli /path/to/dataset.csv /path/to/output_folder

 It then prompts the user to enter the following values:

   - **Num of folds** : The number of folds for the cross-validation run
   - **Test Size** :  The percentage of the dataset values to use as a test set, specified between 0 and 1
   - **Num of Seeds** : The number of MOSES runs per each fold using different random seeds
   - **Target** : The name of the target column in the dataset (defaults to first column)

 You can either specify values for available MOSES options or use the default values. To find out more about the availabe MOSES options run:

            #~ mozi-cli --help
