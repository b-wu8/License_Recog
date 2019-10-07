import cv2
from PIL import Image
from torch import nn, optim
from torch.autograd import Variable
from torchvision import transforms

class neuralnetwork(nn.Module):
    def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
        super(neuralnetwork, self).__init__()
        self.layer1 = nn.Linear(in_dim, n_hidden_1)
        self.layer2 = nn.Linear(n_hidden_1, n_hidden_2)
        self.layer3 = nn.Linear(n_hidden_2, out_dim)

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return x

image = cv2.imread("../pics/JGT5069.jpg", cv2.IMREAD_UNCHANGED)

learning_rate = 1e-2
rep = 20

train_data = image
train_ans = "JGT5069"


model = neuralnetwork(28*28, 300, 100, 10)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr = learning_rate)


resized = cv2.resize(image, (784,300), interpolation=cv2.INTER_AREA)
image = transforms.ToTensor()(resized)


for no in range(rep):
    print("Number {}\n\n".format(no+1))
    img = Variable(image)
    out = model(img)
    # loss = criterion(out, train_ans)

