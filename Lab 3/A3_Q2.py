def main():
    states=[
        {
            'sensor':'Inbound',
            'obstacle':False,
            'emergency':'Neutral'
        },
        {
            'sensor':'Inbound',
            'obstacle':True,
            'emergency':'Neutral'
        },
        {
            'sensor':'Outbound',
            'obstacle':True,
            'emergency':'Neutral'
        },
        {
            'sensor':'Outbound',
            'obstacle':False,
            'emergency':'Neutral'
        },
        {
            'sensor':'Inbound',
            'obstacle':False,
            'emergency':'Active'
        }
    ]
    count=0
    action={}
    for state in states:
        count+=1
        sensor=state['sensor']
        obstacle=state['obstacle']
        emergency=state['emergency']
        if emergency=='Active':
            action['gate']='Lower'
            action['siren']='On'
            action['train_signal']='Red'
        elif sensor=='Inbound':
            action['gate']='Lower'
            action['siren']='On'
            if obstacle:
                action['train_signal']='Red'
            else:
                action['train_signal']='Green'
        else:
            action['gate']='Raise'
            action['siren']='Off'
            action['train_signal']='Green'
        print(f"\nState {count}:-")
        print("Percept: ",state)
        print("Action : ",action)

if __name__=='__main__':
    main()