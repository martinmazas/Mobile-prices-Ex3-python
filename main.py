from task1 import *

# price2 = price - (price/20)
def main():
    suma = Summary("mobile_price_1.csv")
    suma.addResolution()
    suma.dotsPerInch()
    suma.callRatio()
    suma.fromMBToGB()

    # suma.printDescription()
    # suma.getPricesHistogram()
    # suma.dataHeatMap()
    # suma.plotRelationshipWithPrice('resolution')
    # suma.threeCorrelatedFeatures()
    suma.ordinalToNumerical()
    suma.nominalToBinary()
    # suma.dataHeatMap()
    # suma.saveIntoCsvFile()
    # suma.relationshipBetweenFourFeatures('price', 'battery_power', 'px_height', 'px_width')
    suma.plotRelationshipBetweenWidthHeightPriceCore()


if __name__ == '__main__':
    main()

