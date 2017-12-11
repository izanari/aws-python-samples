'''Create NAT Gateway'''
import boto3

SUBNETID='yoursubnetid'

def natgateway_handler():
    ''' nat gatewayを作る '''

    client = boto3.client('ec2')

    response = client.allocate_address(
        Domain='vpc'
    )
    print(response)
    if response["ResponseMetadata"]["HTTPStatusCode"]==200 :
        print("EIPの取得に成功")
        response=client.create_nat_gateway(
          AllocationId=response["AllocationId"],
          SubnetId=SUBNETID
        )
        print(response)

      if response["ResponseMetadata"]["HTTPStatusCode"]==200 :
        print("NATGatewayの作成に成功しました")
        """すぐに使えるわけではないので、statusの確認が必要"""
        print( response["State"] )
        print( response )

    else:
       print("EIPの取得に失敗")


natgateway_handler()
