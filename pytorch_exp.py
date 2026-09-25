import torch
import torch.nn as nn

class model(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(2, 4),
            nn.ReLU(),
            nn.Linear(4, 3)
        )
    def forward(self, x):
        return self.network(x)



model = model()


X = torch.tensor([
    # Class 0
    [1.0, 1.0],
    [1.0, 2.0],
    [2.0, 1.0],
    [2.0, 2.0],
    [1.5, 1.0],

    # Class 1
    [5.0, 1.0],
    [6.0, 1.0],
    [5.0, 2.0],
    [6.0, 2.0],
    [5.5, 1.5],

    # Class 2
    [3.0, 5.0],
    [4.0, 5.0],
    [3.0, 6.0],
    [4.0, 6.0],
    [3.5, 5.5],
])

y = torch.tensor([
    # Class 0
    0, 0, 0, 0, 0,

    # Class 1
    1, 1, 1, 1, 1,

    # Class 2
    2, 2, 2, 2, 2
])

class MyDataset(torch.utils.data.Dataset):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]

dataset = MyDataset(X, y)
loader = torch.utils.data.DataLoader(dataset, batch_size=4, shuffle=True)

optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
for epoch in range(2000):
    for x, y in loader:
        predictions = model(x)
        loss = nn.CrossEntropyLoss()(predictions, y)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

test_X = torch.tensor([
    [1.5, 1.5],   # should be class 0
    [2.0, 1.5],   # should be class 0

    [5.5, 1.5],   # should be class 1
    [5.0, 2.0],   # should be class 1

    [3.5, 5.2],   # should be class 2
    [3.0, 5.5],   # should be class 2

    # a little farther from training points
    [1.8, 1.8],   # class 0
    [5.8, 1.8],   # class 1
    [3.8, 5.8],   # class 2
])

test_y = torch.tensor([
    0,
    0,
    1,
    1,
    2,
    2,
    0,
    1,
    2
])

model.eval()

with torch.no_grad():
    logits = model(test_X)

    predections = torch.argmax(logits, dim=1)

print("Predections: ", predections)
print("Actual: ", test_y)

