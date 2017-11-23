from llxquant.assets import  asset

class single_proposal(dict):
    def __init__(self,thedate,*arg,**kwargs):
        super(single_proposal,self).__init__(*arg,**kwargs)
        self.thedate=thedate
        assert self.check_data()


    def check_data(self):
        for k in self.keys():
            assert issubclass(type(k),asset)
        return True

    def add_proposal(self,asset_instance,percentage):
        if asset_instance not in self.keys():
            self[asset_instance]=percentage
        else:
            self[asset_instance]+=percentage



class proposal(dict):
    def __init__(self,*arg,**kwargs):
        super(proposal, self).__init__(*arg, **kwargs)
        assert  self.check_data()

    def check_data(self):
        for k,v in self:
            v.check_data()


    def add_poposal(self,thedate,proposal):
        assert isinstance(proposal,single_proposal)
        if thedate in self.keys():
            raise ValueError('thedate {} is already in the proposal calendar'.format(thedate))
        else:
            self[thedate]=proposal

