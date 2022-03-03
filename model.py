import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
import torch
import torchvision.models._utils as _utils


class HeadNet(nn.Module):
    def __init__(self):
        super(HeadNet, self).__init__()
        self.model = models.resnet50(pretrained=True)
        self.model = nn.Sequential(*list(self.model.children())[:-5])
    def forward(self,x):
        return self.model(x)
    
class SubNet(nn.Module):
    def __init__(self,num_class):
        super(SubNet, self).__init__()
        self.model = models.resnet50(pretrained=True)
        self.model = nn.Sequential(*list(self.model.children())[-5:-1])
        self.fc = nn.Linear(in_features=2048, out_features=num_class, bias=True)
    def forward(self,x):
        x=self.model(x)
        x=x.view(x.size(0), -1)
        x=self.fc(x)
        return x        
    
        
class Multi_Classification_Model(nn.Module):
    def __init__(self, output_feature_list):
        super(Multi_Classification_Model,self).__init__()
        self.net_list=[]
        self.class_list=output_feature_list
        self.head = HeadNet()    
        self.out_features = []
        for i,cls_n in enumerate(self.class_list):
            self.net_list.append('sub_'+str(i+1))
            exec('self.sub_{} = SubNet({})'.format(i+1,cls_n))

    def forward(self,inputs):
        out = self.head(inputs) #pretrained model

        for i, net in enumerate(self.net_list):
            exec('feature{} = self.{}(out)'.format(i+1,net))
            self.out_features.append(exec('feature{}'.format(i+1)))
            
        return self.out_features
        
net = Multi_Classification_Model(output_feature_list=[3,3,3])

print('========================================================================================================')
print(' '*40+'Model Architecture')
print('========================================================================================================')
print(net)
