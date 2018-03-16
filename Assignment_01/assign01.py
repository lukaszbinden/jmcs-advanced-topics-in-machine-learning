# Notice that in this assignment you are not allowed to use torch optimizer and nn module.
import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
from math import log10

# Hyper Parameters 
input_size = 784
hidden_size = 128
num_epochs = 10
batch_size = 100
learning_rate = 0.001

# MNIST Dataset 
train_dataset = dsets.MNIST(root='./data', 
                            train=True, 
                            transform=transforms.ToTensor(),  
                            download=True)

test_dataset = dsets.MNIST(root='./data', 
                           train=False, 
                           transform=transforms.ToTensor())

# Data Loader (Input Pipeline)
train_loader = torch.utils.data.DataLoader(dataset=train_dataset, 
                                           batch_size=batch_size, 
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset, 
                                          batch_size=batch_size, 
                                          shuffle=False)

# initialize your parameters
# W1 = 
# W2 = 


# Train the Model
for epoch in range(num_epochs):
    for i, (images, -,) in enumerate(train_loader):  
        # Convert torch tensor to Variable
        images = images.view(-1, 28*28)
        targets = images.clone()
        # forward 

        # loss calculation
        loss = 
        # gradient calculation and update parameters

        # check your loss 
        if (i+1) % 1 == 0:
            print ('Epoch [%d/%d], Step [%d/%d], Loss: %.4f' 
                   %(epoch+1, num_epochs, i+1, len(train_dataset)//batch_size, loss))

# Test the Model
avg_psnr = 0
for (images, -,) in test_loader:
    images = images.view(-1, 28*28)
    targets = images.clone()
    # get your predictions
    predictions = 
    # calculate PSNR
    # mse = torch.mean((predictions - targets).pow(2))
    # psnr = 10 * log10(1 / mse)
    avg_psnr += psnr
print("===> Avg. PSNR: {:.4f} dB".format(avg_psnr / len(test_loader)))