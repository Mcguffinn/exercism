import string
def word_count(phrase):
    word_count = {}

    for word in word_cleaner(phrase):
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    return word_count
   
def word_cleaner(phrase):
    exclude = set('!&@$%^&:.')
    phrase = ''.join(ch for ch in phrase if ch not in exclude)
    phrase = phrase.lower().replace(',',' ').replace('_',' ').split()

    for asshat in phrase:
         yield asshat.strip("'")
    




def blade_runner():
    x = '''


    Home>
    Storage

    MyDigitalSSD M2X M.2 NVMe SSD Enclosure Review - A PCIe to USB Storage Bridge
    by Ganesh T S on October 31, 2018 8:00 AM EST

        Posted in
        Storage
        SSDs
        USB 3.1
        NVMe
        Type-C
        Storage Bridge
        External SSDs

    26
    Comments
    + Add A
    Comment

    Storage bridges come in many varieties within the internal and external market segments. USB has become the de-facto standard when it comes to external mass-market storage enclosures. But while there are plenty of options to bridge SATA devices in different form factors to USB, the rapid rise in popularity of NVMe drives has brought about a different challenge. In the premium market, we have many Thunderbolt 3 external SSDs with M.2 NVMe drives inside. However for various reasons, the development of NVMe-to-USB adapters has been another matter.
    In fact it's only recently that we've finally seen some progress on this front. JMicron's introduction of a PCIe 3.0 x2 to USB 3.1 Gen 2 bridge chip (JMS583) has enabled Asian OEMs to introduce bus-powered NVMe SSD enclosures with a USB interface, finally enabling relatively cheap USB adapters for NVMe drives. MyDigitalSSD, in turn, is one of the first to bring such a device to the North American market with their M2X External USB 3.1 Gen 2 M.2 NVMe PCIe SSD Enclosure Adapter.
        '''

    return word_count(x)


def main():
    result = blade_runner()
    print(result)
if __name__ == '__main__':
    main()







































