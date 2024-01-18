Rock Paper Scissors Image Recognition Project

github link: https://github.com/Polyakri/projects/edit/main/MachineLearningProjects/RockPaperScissors_Game

Overview

This GitHub project focuses on creating a robust image recognition model for the classic game of Rock, Paper, Scissors. The objective is to develop a model that can accurately recognize and respond with the winning hand gesture based on input images.
Dataset

The dataset used for this project is sourced from Kaggle. It contains a variety of images for Rock, Paper, and Scissors gestures.
Steps:

    Read and Create Dataset:
        Download the dataset from the provided Kaggle link.
        Organize the dataset and ensure proper folder structure.
        Read the data and preprocess it for model training.

    ANNs with PCA (Principal Component Analysis):
        Implement Artificial Neural Networks (ANNs) with PCA for dimensionality reduction.
        Train multiple ANN models with varying parameters.
        Evaluate and compare their accuracies using the provided CSV files.

    Model Training:
        Train different ANN models without PCA, experimenting with architectures and hyperparameters.
        Choose the model with the highest accuracy for further evaluation.

    Convolutional Neural Network (CNN) Training:
        Implement and train a Convolutional Neural Network on the original image data.
        Evaluate the CNN's performance and compare it with the best-performing ANN.

    Game Simulation:
        Develop a game simulation where an agent selects an image.
        Introduce noise to the selected image.
        Utilize the trained model to predict the image and determine the winning hand gesture.

Results

After extensive experimentation with around 3000 models, the best-performing model achieved an accuracy of 99.5%. The evaluation results are provided in the CSV files within the project.


Author

    Polydoros Akritidis


Feel free to reach out to the author for any questions or collaborations.

Happy Coding!
