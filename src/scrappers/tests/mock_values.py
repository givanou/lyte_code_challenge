import json
from unittest.mock import MagicMock

api_response_value = json.dumps(
{
    '_embedded': {
        'events': [{
            'name': 'Shania Twain "Let\'s Go!" - The Las Vegas Residency',
            'type': 'event',
            'id': '1AyZA-7GkdE1hoj',
            'test': False,
            'url': 'https://www.ticketmaster.com/shania-twain-lets-go-the-las-las-vegas-nevada-12-12-2020/event/39005844E729B45C',
            'locale': 'en-us',
            'images': [{
                'ratio': '16_9',
                'url': 'https://s1.ticketm.net/dam/a/1ba/422e077f-a762-48ff-9573-7d30917b51ba_1084491_TABLET_LANDSCAPE_LARGE_16_9.jpg',
                'width': 2048,
                'height': 1152,
                'fallback': False
            }],
            'sales': {
                'public': {
                    'startDateTime': '2020-02-14T18:00:00Z',
                    'startTBD': False,
                    'endDateTime': '2020-12-13T05:00:00Z'
                }
            },
            'dates': {
                'start': {
                    'localDate': '2020-12-12',
                    'localTime': '20:00:00',
                    'dateTime': '2020-12-13T04:00:00Z',
                    'dateTBD': False,
                    'dateTBA': False,
                    'timeTBA': False,
                    'noSpecificTime': False
                },
                'timezone': 'America/Los_Angeles',
                'status': {
                    'code': 'onsale'
                },
                'spanMultipleDays': False
            },
            'classifications': [{
                'primary': True,
                'segment': {
                    'id': 'KZFzniwnSyZfZ7v7nJ',
                    'name': 'Music'
                },
                'genre': {
                    'id': 'KnvZfZ7vAv6',
                    'name': 'Country'
                },
                'subGenre': {
                    'id': 'KZazBEonSMnZfZ7vAFa',
                    'name': 'Country'
                },
                'type': {
                    'id': 'KZAyXgnZfZ7v7nI',
                    'name': 'Undefined'
                },
                'subType': {
                    'id': 'KZFzBErXgnZfZ7v7lJ',
                    'name': 'Undefined'
                },
                'family': False
            }],
            'promoter': {
                'id': '653',
                'name': 'LIVE NATION MUSIC',
                'description': 'LIVE NATION MUSIC / NTL / USA'
            },
            'promoters': [{
                'id': '653',
                'name': 'LIVE NATION MUSIC',
                'description': 'LIVE NATION MUSIC / NTL / USA'
            }],
            'pleaseNote': 'Patrons are permitted to stand during performance. Recommended ages 6+. All patrons must have a ticket regardless of age. GROUPS: Orders of 10 or more should be referred to the Group Sales department at 1-866-574-3851 or email EntertainmentGroupSales@Caesars.com The venue reserves the right to implement security procedures designed to protect the experience for all of our customers.',
            'priceRanges': [{
                'type': 'standard',
                'currency': 'USD',
                'min': 60.0,
                'max': 251.0
            }],
            'products': [{
                'id': '1AyZA-kGkd5Wv7H',
                'url': 'https://www.ticketmaster.com/were-having-a-party-vip-package-las-vegas-nevada-12-12-2020/event/39005846CBF4113C',
                'type': 'Upsell',
                'name': '"We\'re Having a Party" VIP Package - Add To Any Ticket'
            }, {
                'id': '1AyZA-kGkd5Xv7X',
                'url': 'https://www.ticketmaster.com/the-lets-go-behind-the-scenes-las-vegas-nevada-12-12-2020/event/39005846CBF8113E',
                'type': 'Upsell',
                'name': 'The "Let\'s Go" Behind the Scenes VIP Package - Add To Any Ticket'
            }, {
                'id': '1AyZA-kGkdepov1',
                'url': 'https://www.ticketmaster.com/come-on-over-vip-package-add-las-vegas-nevada-12-12-2020/event/39005846C259104A',
                'type': 'Upsell',
                'name': '"Come On Over" VIP Package - Add to Any Ticket - Must Buy Two'
            }],
            'seatmap': {
                'staticUrl': 'https://maps.ticketmaster.com/maps/geometry/3/event/39005844E729B45C/staticImage?type=png&systemId=HOST'
            },
            'ticketLimit': {
                'info': 'VIP Packages must buy 6. There is a 9 ticket limit for this event.'
            },
            'ageRestrictions': {
                'legalAgeEnforced': False
            },
            '_links': {
                'self': {
                    'href': '/discovery/v2/events/1AyZA-7GkdE1hoj?locale=en-us'
                },
                'attractions': [{
                    'href': '/discovery/v2/attractions/K8vZ91719n0?locale=en-us'
                }],
                'venues': [{
                    'href': '/discovery/v2/venues/KovZpZAJalEA?locale=en-us'
                }]
            },
            '_embedded': {
                'venues': [{
                    'name': 'Zappos Theater at Planet Hollywood',
                    'type': 'venue',
                    'id': 'KovZpZAJalEA',
                    'test': False,
                    'url': 'https://www.ticketmaster.com/zappos-theater-at-planet-hollywood-tickets-las-vegas/venue/467893',
                    'locale': 'en-us',
                    'aliases': ['axis theater'],
                    'images': [{
                        'ratio': '16_9',
                        'url': 'https://s1.ticketm.net/dbimages/21797v.jpg',
                        'width': 205,
                        'height': 115,
                        'fallback': False
                    }],
                    'postalCode': '89109',
                    'timezone': 'America/Los_Angeles',
                    'city': {
                        'name': 'Las Vegas'
                    },
                    'state': {
                        'name': 'Nevada',
                        'stateCode': 'NV'
                    },
                    'country': {
                        'name': 'United States Of America',
                        'countryCode': 'US'
                    },
                    'address': {
                        'line1': '3667 S Las Vegas Blvd'
                    },
                    'location': {
                        'longitude': '-115.17247058',
                        'latitude': '36.10961689'
                    },
                    'markets': [{
                        'name': 'Las Vegas',
                        'id': '14'
                    }],
                    'dmas': [{
                        'id': 319
                    }],
                    'boxOfficeInfo': {
                        'phoneNumberDetail': '1-855-234-7469 1-866-574-3851 - Group Sales (10+)',
                        'openHoursDetail': '10:00am - 8:00pm (show nights vary)',
                        'acceptedPaymentDetail': 'Cash and All Major Credit Cards',
                        'willCallDetail': 'Must have photo ID & credit card used to purchase tickets when picking up will call tickets'
                    },
                    'parkingDetail': 'Fees may apply.',
                    'accessibleSeatingDetail': 'Accessible ramps to orchestra & mezzanine sections; Elevator service to balcony',
                    'generalInfo': {
                        'generalRule': 'This is a non-smoking showroom, no outside food or beverage',
                        'childRule': 'All patrons need to have a ticket *Age limits may vary for special events'
                    },
                    'upcomingEvents': {
                        '_total': 63,
                        'ticketmaster': 63
                    },
                    '_links': {
                        'self': {
                            'href': '/discovery/v2/venues/KovZpZAJalEA?locale=en-us'
                        }
                    }
                }],
                'attractions': [{
                    'name': 'Shania Twain',
                    'type': 'attraction',
                    'id': 'K8vZ91719n0',
                    'test': False,
                    'url': 'https://www.ticketmaster.com/shania-twain-tickets/artist/764367',
                    'locale': 'en-us',
                    'externalLinks': {
                        'youtube': [{
                            'url': 'https://www.youtube.com/user/ShaniaTwain'
                        }],
                        'twitter': [{
                            'url': 'https://twitter.com/FollowShania'
                        }],
                        'lastfm': [{
                            'url': 'http://www.last.fm/music/Shania+Twain'
                        }],
                        'facebook': [{
                            'url': 'https://www.facebook.com/ShaniaTwain'
                        }],
                        'wiki': [{
                            'url': 'https://en.wikipedia.org/wiki/Shania_Twain'
                        }],
                        'musicbrainz': [{
                            'id': 'faabb55d-3c9e-4c23-8779-732ac2ee2c0d'
                        }],
                        'homepage': [{
                            'url': 'http://www.shaniatwain.com/'
                        }]
                    },
                    'aliases': ['shaina twain', 'shania twain', 'shinia twain'],
                    'images': [{
                        'ratio': '16_9',
                        'url': 'https://s1.ticketm.net/dam/a/1ba/422e077f-a762-48ff-9573-7d30917b51ba_1084491_TABLET_LANDSCAPE_LARGE_16_9.jpg',
                        'width': 2048,
                        'height': 1152,
                        'fallback': False
                    }],
                    'classifications': [{
                        'primary': True,
                        'segment': {
                            'id': 'KZFzniwnSyZfZ7v7nJ',
                            'name': 'Music'
                        },
                        'genre': {
                            'id': 'KnvZfZ7vAv6',
                            'name': 'Country'
                        },
                        'subGenre': {
                            'id': 'KZazBEonSMnZfZ7vAFa',
                            'name': 'Country'
                        },
                        'type': {
                            'id': 'KZAyXgnZfZ7v7nI',
                            'name': 'Undefined'
                        },
                        'subType': {
                            'id': 'KZFzBErXgnZfZ7v7lJ',
                            'name': 'Undefined'
                        },
                        'family': False
                    }],
                    'upcomingEvents': {
                        '_total': 23,
                        'ticketmaster': 23
                    },
                    '_links': {
                        'self': {
                            'href': '/discovery/v2/attractions/K8vZ91719n0?locale=en-us'
                        }
                    }
                }]
            }
        }, {
            'name': 'New York Yankees v. Houston Astros',
            'type': 'event',
            'id': 'G5vVZ4U9eK3Gh',
            'test': False,
            'url': 'https://www.ticketmaster.com/new-york-yankees-v-houston-astros-bronx-new-york-09-21-2020/event/1D005765C24D231B',
            'locale': 'en-us',
            'images': [{
                'ratio': '4_3',
                'url': 'https://s1.ticketm.net/dam/a/951/8971a259-74a9-4412-a0f4-6c3cf9731951_899911_CUSTOM.jpg',
                'width': 305,
                'height': 225,
                'fallback': False
            }],
            'sales': {
                'public': {
                    'startDateTime': '2020-02-24T15:00:00Z',
                    'startTBD': False,
                    'endDateTime': '2020-09-21T23:05:00Z'
                },
                'presales': [{
                    'startDateTime': '2020-02-18T15:00:00Z',
                    'endDateTime': '2020-02-24T03:00:00Z',
                    'name': 'NYY Premium Licensees'
                }, {
                    'startDateTime': '2020-02-18T17:00:00Z',
                    'endDateTime': '2020-02-24T03:00:00Z',
                    'name': 'NYY Full Season Licensees'
                }, {
                    'startDateTime': '2020-02-18T19:00:00Z',
                    'endDateTime': '2020-02-24T03:00:00Z',
                    'name': 'NYY Partial Plan Licensees'
                }, {
                    'startDateTime': '2020-02-18T21:00:00Z',
                    'endDateTime': '2020-02-24T03:00:00Z',
                    'name': 'NYY Group Leaders'
                }, {
                    'startDateTime': '2020-02-19T15:00:00Z',
                    'endDateTime': '2020-02-24T03:00:00Z',
                    'name': 'Mastercard Cardholders Presale'
                }]
            },
            'dates': {
                'start': {
                    'localDate': '2020-09-21',
                    'localTime': '19:05:00',
                    'dateTime': '2020-09-21T23:05:00Z',
                    'dateTBD': False,
                    'dateTBA': False,
                    'timeTBA': False,
                    'noSpecificTime': False
                },
                'timezone': 'America/New_York',
                'status': {
                    'code': 'onsale'
                },
                'spanMultipleDays': False
            },
            'classifications': [{
                'primary': True,
                'segment': {
                    'id': 'KZFzniwnSyZfZ7v7nE',
                    'name': 'Sports'
                },
                'genre': {
                    'id': 'KnvZfZ7vAdv',
                    'name': 'Baseball'
                },
                'subGenre': {
                    'id': 'KZazBEonSMnZfZ7vF1n',
                    'name': 'MLB'
                },
                'type': {
                    'id': 'KZAyXgnZfZ7v7l1',
                    'name': 'Group'
                },
                'subType': {
                    'id': 'KZFzBErXgnZfZ7vA7d',
                    'name': 'Team'
                },
                'family': False
            }],
            'promoter': {
                'id': '685',
                'name': 'MLB REGULAR SEASON',
                'description': 'MLB REGULAR SEASON / NTL / USA'
            },
            'promoters': [{
                'id': '685',
                'name': 'MLB REGULAR SEASON',
                'description': 'MLB REGULAR SEASON / NTL / USA'
            }],
            'info': 'Please note that protective netting of varying heights is used in the Stadium from Section 011 to behind home plate to Section 029. If you purchase tickets, you may receive customer service messages via email from the New York Yankees, including optional surveys regarding your baseball experience. Ticket holder assumes all risk of injury from balls and bats entering the stands. For more information on which seating sections have netting or screening in front of them, please visit yankees.com/netting.',
            'pleaseNote': 'All ticket verification QR codes will appear 48 hours prior to the scheduled start of the game. If you purchased your tickets as a gift, please download and print a holiday gift certificate to present to your gift recipient at yankees.com/priceless. All individual game ticket prices are subject to variable and dynamic pricing, which provide fans with more price options based on changing factors that affect market demand.',
            'priceRanges': [{
                'type': 'standard',
                'currency': 'USD',
                'min': 25.0,
                'max': 510.0
            }],
            'seatmap': {
                'staticUrl': 'https://maps.ticketmaster.com/maps/geometry/3/event/1D005765C24D231B/staticImage?type=png&systemId=HOST'
            },
            'accessibility': {
                'info': 'Yankee Stadium management strives to provide an accessible environment for all its Guests. Wheelchair accessible and aisle-transfer (semi-ambulatory) seats are offered at various price points and locations, pending availability, throughout the Stadium and include the Yankees Premium seat locations. The Stadium also offers enhanced accessibility for Guests with hearing loss or low vision and for Guests who are deaf or blind. \r\nPlease select the location or price point as indicated in your search that best fits your needs to view available options. You may then select and purchase seats that are available through Ticketmaster. \r\nNotwithstanding, if you would like more details or if you have any questions regarding wheelchair accessible and/or aisle-transfer seating, you may contact Disabled Services at Yankee Stadium at (718) 579-4510 (voice) or (718) 579-4595 (TTY) or email disabledservices@yankees.com. \r\nNew York Yankees Ticket Office Hours: Monday-Saturday 9am-5pm, Sunday 10am-4pm'
            },
            'ticketLimit': {
                'info': 'Only a LIMITED number of Tickets (as determined by the Yankees in its sole and absolute discretion) will be made available. Max of 19, (eight for presales), Tickets to each potential game scheduled to be played during the 2020 Regular Season.'
            },
            'ageRestrictions': {
                'legalAgeEnforced': False
            },
            '_links': {
                'self': {
                    'href': '/discovery/v2/events/G5vVZ4U9eK3Gh?locale=en-us'
                },
                'attractions': [{
                    'href': '/discovery/v2/attractions/K8vZ9171okV?locale=en-us'
                }, {
                    'href': '/discovery/v2/attractions/K8vZ91718zV?locale=en-us'
                }],
                'venues': [{
                    'href': '/discovery/v2/venues/KovZpZA6t77A?locale=en-us'
                }]
            },
            '_embedded': {
                'venues': [{
                    'name': 'Yankee Stadium',
                    'type': 'venue',
                    'id': 'KovZpZA6t77A',
                    'test': False,
                    'url': 'https://www.ticketmaster.com/yankee-stadium-tickets-bronx/venue/237572',
                    'locale': 'en-us',
                    'images': [{
                        'ratio': '16_9',
                        'url': 'https://s1.ticketm.net/dbimages/16603v.jpg',
                        'width': 205,
                        'height': 115,
                        'fallback': False
                    }],
                    'postalCode': '10451',
                    'timezone': 'America/New_York',
                    'city': {
                        'name': 'Bronx'
                    },
                    'state': {
                        'name': 'New York',
                        'stateCode': 'NY'
                    },
                    'country': {
                        'name': 'United States Of America',
                        'countryCode': 'US'
                    },
                    'address': {
                        'line1': '1 East 161st Street'
                    },
                    'location': {
                        'longitude': '-73.9276264',
                        'latitude': '40.8285237'
                    },
                    'markets': [{
                        'name': 'New York/Tri-State Area',
                        'id': '35'
                    }, {
                        'name': 'Northern New Jersey',
                        'id': '55'
                    }, {
                        'name': 'Connecticut',
                        'id': '124'
                    }],
                    'dmas': [{
                        'id': 296
                    }, {
                        'id': 345
                    }, {
                        'id': 422
                    }],
                    'parkingDetail': 'PREPAID PARKING The Yankees neither control nor operate the parking lots and garages surrounding the Stadium and are not responsible for setting parking lot rates, refund policies, rules and/or procedures. Quik Park was granted those rights, including responsibility for establishing and controlling parking rates, refund policies, rules and/or procedures, by New York City.',
                    'upcomingEvents': {
                        '_total': 551,
                        'ticketmaster': 551
                    },
                    'ada': {
                        'adaPhones': 'Disabled Services at Yankee Stadium: (718) 579-4510 (voice) or (718) 579-4595 (TTY) \nEmail disabledservices@yankees.com.\n',
                        'adaCustomCopy': 'Yankee Stadium management strives to provide an accessible environment for all its Guests. Wheelchair accessible and aisle-transfer (semi-ambulatory) seats are offered at various price points and locations, pending availability, throughout the Stadium and include the Yankees Premium seat locations. The Stadium also offers enhanced accessibility for Guests with hearing loss or low vision and for Guests who are deaf or blind. \nPlease select the location or price point as indicated in your search that best fits your needs to view available options.  You may then select and purchase seats that are available through Ticketmaster including its website.  \nNotwithstanding, if you would like more details or if you have any questions regarding wheelchair accessible and/or aisle-transfer seating, you may contact Disabled Services at Yankee Stadium at (718) 579-4510 (voice) or (718) 579-4595 (TTY) or email disabledservices@yankees.com.\n\n',
                        'adaHours': 'New York Yankees Ticket Office Hours: \nMonday - Saturday 9:00am - 5:00pm \nSunday 10:00am - 4:00pm\n\n   \n'
                    },
                    '_links': {
                        'self': {
                            'href': '/discovery/v2/venues/KovZpZA6t77A?locale=en-us'
                        }
                    }
                }],
                'attractions': [{
                    'name': 'New York Yankees',
                    'type': 'attraction',
                    'id': 'K8vZ9171okV',
                    'test': False,
                    'url': 'https://www.ticketmaster.com/new-york-yankees-tickets/artist/805992',
                    'locale': 'en-us',
                    'images': [{
                        'ratio': '4_3',
                        'url': 'https://s1.ticketm.net/dam/a/951/8971a259-74a9-4412-a0f4-6c3cf9731951_899911_CUSTOM.jpg',
                        'width': 305,
                        'height': 225,
                        'fallback': False
                    }],
                    'classifications': [{
                        'primary': True,
                        'segment': {
                            'id': 'KZFzniwnSyZfZ7v7nE',
                            'name': 'Sports'
                        },
                        'genre': {
                            'id': 'KnvZfZ7vAdv',
                            'name': 'Baseball'
                        },
                        'subGenre': {
                            'id': 'KZazBEonSMnZfZ7vF1n',
                            'name': 'MLB'
                        },
                        'type': {
                            'id': 'KZAyXgnZfZ7v7l1',
                            'name': 'Group'
                        },
                        'subType': {
                            'id': 'KZFzBErXgnZfZ7vA7d',
                            'name': 'Team'
                        },
                        'family': False
                    }],
                    'upcomingEvents': {
                        '_total': 231,
                        'ticketmaster': 231
                    },
                    '_links': {
                        'self': {
                            'href': '/discovery/v2/attractions/K8vZ9171okV?locale=en-us'
                        }
                    }
                }, {
                    'name': 'Houston Astros',
                    'type': 'attraction',
                    'id': 'K8vZ91718zV',
                    'test': False,
                    'url': 'https://www.ticketmaster.com/houston-astros-tickets/artist/805948',
                    'locale': 'en-us',
                    'images': [{
                        'ratio': '4_3',
                        'url': 'https://s1.ticketm.net/dam/a/140/e6d19d99-c1d0-48d6-8bbe-6296c4ef1140_1255211_CUSTOM.jpg',
                        'width': 305,
                        'height': 225,
                        'fallback': False,
                        'attribution': 'TM Generic'
                    }],
                    'classifications': [{
                        'primary': True,
                        'segment': {
                            'id': 'KZFzniwnSyZfZ7v7nE',
                            'name': 'Sports'
                        },
                        'genre': {
                            'id': 'KnvZfZ7vAdv',
                            'name': 'Baseball'
                        },
                        'subGenre': {
                            'id': 'KZazBEonSMnZfZ7vF1n',
                            'name': 'MLB'
                        },
                        'type': {
                            'id': 'KZAyXgnZfZ7v7l1',
                            'name': 'Group'
                        },
                        'subType': {
                            'id': 'KZFzBErXgnZfZ7vA7d',
                            'name': 'Team'
                        },
                        'family': False
                    }],
                    'upcomingEvents': {
                        '_total': 29,
                        'ticketmaster': 29
                    },
                    '_links': {
                        'self': {
                            'href': '/discovery/v2/attractions/K8vZ91718zV?locale=en-us'
                        }
                    }
                }]
            }
        }, {
            'name': 'Hamilton (Touring)',
            'type': 'event',
            'id': 'G5dIZpkRFo0VK',
            'test': False,
            'url': 'https://www.ticketmaster.com/hamilton-touring-houston-texas-08-02-2020/event/3A00586BC8464D13',
            'locale': 'en-us',
            'images': [{
                'ratio': '16_9',
                'url': 'https://s1.ticketm.net/dam/a/300/88bcb3d0-aa78-428d-ad10-52514ea72300_570131_EVENT_DETAIL_PAGE_16_9.jpg',
                'width': 205,
                'height': 115,
                'fallback': False
            }],
            'sales': {
                'public': {
                    'startDateTime': '2020-04-03T15:00:00Z',
                    'startTBD': False,
                    'endDateTime': '2020-08-02T19:00:00Z'
                },
                'presales': [{
                    'startDateTime': '2020-04-01T15:00:00Z',
                    'endDateTime': '2020-04-02T22:00:00Z',
                    'name': 'PRESALE'
                }, {
                    'startDateTime': '2020-04-02T15:00:00Z',
                    'endDateTime': '2020-04-02T22:00:00Z',
                    'name': 'PRESALE 2'
                }]
            },
            'dates': {
                'start': {
                    'localDate': '2020-08-02',
                    'localTime': '14:00:00',
                    'dateTime': '2020-08-02T19:00:00Z',
                    'dateTBD': False,
                    'dateTBA': False,
                    'timeTBA': False,
                    'noSpecificTime': False
                },
                'timezone': 'America/Chicago',
                'status': {
                    'code': 'onsale'
                },
                'spanMultipleDays': False
            },
            'classifications': [{
                'primary': True,
                'segment': {
                    'id': 'KZFzniwnSyZfZ7v7na',
                    'name': 'Arts & Theatre'
                },
                'genre': {
                    'id': 'KnvZfZ7v7l1',
                    'name': 'Theatre'
                },
                'subGenre': {
                    'id': 'KZazBEonSMnZfZ7vAve',
                    'name': 'Musical'
                },
                'type': {
                    'id': 'KZAyXgnZfZ7v7nI',
                    'name': 'Undefined'
                },
                'subType': {
                    'id': 'KZFzBErXgnZfZ7v7lJ',
                    'name': 'Undefined'
                },
                'family': False
            }],
            'promoter': {
                'id': '819',
                'name': 'DO NOT USE',
                'description': 'DO NOT USE / NTL / USA'
            },
            'promoters': [{
                'id': '819',
                'name': 'DO NOT USE',
                'description': 'DO NOT USE / NTL / USA'
            }],
            'info': 'All patrons, including infants and lap children, must have a ticket. There will be an audio described performance Sunday, July 12 at 2:00pm and Sunday, July 26 at 2:00pm. There will be an open captioned performance Saturday, July 11 at 2:00pm. There will be an ASLI performance Sunday, August 2 at 8:00pm.',
            'pleaseNote': 'There is a delivery delay in place until May 1, 2020. All patrons, including infants and lap children, must have a ticket. There will be an audio described performance Sunday, July 12 at 2:00pm and Sunday, July 26 at 2:00pm. There will be an open captioned performance Saturday, July 11 at 2:00pm. There will be an ASLI performance Sunday, August 2 at 8:00pm.',
            'priceRanges': [{
                'type': 'standard',
                'currency': 'USD',
                'min': 74.0,
                'max': 394.0
            }],
            'seatmap': {
                'staticUrl': 'https://maps.ticketmaster.com/maps/geometry/3/event/3A00586BC8464D13/staticImage?type=png&systemId=HOST'
            },
            'accessibility': {
                'info': 'For questions regarding accessible seating, please follow the link.'
            },
            'ticketLimit': {
                'info': 'There is an eight (8) ticket limit for the Houston performances from June 30, 2020 to August 9, 2020.'
            },
            'ageRestrictions': {
                'legalAgeEnforced': False
            },
            '_links': {
                'self': {
                    'href': '/discovery/v2/events/G5dIZpkRFo0VK?locale=en-us'
                },
                'attractions': [{
                    'href': '/discovery/v2/attractions/K8vZ9174wRf?locale=en-us'
                }],
                'venues': [{
                    'href': '/discovery/v2/venues/KovZpZAJJEaA?locale=en-us'
                }]
            },
            '_embedded': {
                'venues': [{
                    'name': 'Hobby Center',
                    'type': 'venue',
                    'id': 'KovZpZAJJEaA',
                    'test': False,
                    'url': 'https://www.ticketmaster.com/hobby-center-tickets-houston/venue/475611',
                    'locale': 'en-us',
                    'images': [{
                        'ratio': '16_9',
                        'url': 'https://s1.ticketm.net/dbimages/21577v.jpg',
                        'width': 205,
                        'height': 115,
                        'fallback': False
                    }],
                    'postalCode': '77002',
                    'timezone': 'America/Chicago',
                    'city': {
                        'name': 'Houston'
                    },
                    'state': {
                        'name': 'Texas',
                        'stateCode': 'TX'
                    },
                    'country': {
                        'name': 'United States Of America',
                        'countryCode': 'US'
                    },
                    'address': {
                        'line1': '800 Bagby'
                    },
                    'location': {
                        'longitude': '-95.368798',
                        'latitude': '29.7617639'
                    },
                    'markets': [{
                        'name': 'Houston and More',
                        'id': '22'
                    }],
                    'dmas': [{
                        'id': 300
                    }],
                    'boxOfficeInfo': {
                        'openHoursDetail': '10 am - 6 pm Monday - Friday (non-show days)',
                        'acceptedPaymentDetail': 'Visa, MC, AMEX,DSC,Cash,Travelers Checks',
                        'willCallDetail': 'Will call 2 hours prior to curtain time.'
                    },
                    'parkingDetail': 'Traveling east on Rusk (before you reach the theatre onthe right), or traveling west on Walker (after the theatre on the right). There is also ample parking in the underground City Hall and Theater District parking lots (signs are marked with a large star).',
                    'generalInfo': {
                        'generalRule': 'No smoking inside.',
                        'childRule': 'Everyone must have a ticket to enter the theatre.'
                    },
                    'upcomingEvents': {
                        '_total': 62,
                        'ticketmaster': 62
                    },
                    '_links': {
                        'self': {
                            'href': '/discovery/v2/venues/KovZpZAJJEaA?locale=en-us'
                        }
                    }
                }],
                'attractions': [{
                    'name': 'Hamilton (Touring)',
                    'type': 'attraction',
                    'id': 'K8vZ9174wRf',
                    'test': False,
                    'url': 'https://www.ticketmaster.com/hamilton-touring-tickets/artist/2336213',
                    'locale': 'en-us',
                    'images': [{
                        'ratio': '16_9',
                        'url': 'https://s1.ticketm.net/dam/a/300/88bcb3d0-aa78-428d-ad10-52514ea72300_570131_EVENT_DETAIL_PAGE_16_9.jpg',
                        'width': 205,
                        'height': 115,
                        'fallback': False
                    }],
                    'classifications': [{
                        'primary': True,
                        'segment': {
                            'id': 'KZFzniwnSyZfZ7v7na',
                            'name': 'Arts & Theatre'
                        },
                        'genre': {
                            'id': 'KnvZfZ7v7l1',
                            'name': 'Theatre'
                        },
                        'subGenre': {
                            'id': 'KZazBEonSMnZfZ7vAve',
                            'name': 'Musical'
                        },
                        'type': {
                            'id': 'KZAyXgnZfZ7v7nI',
                            'name': 'Undefined'
                        },
                        'subType': {
                            'id': 'KZFzBErXgnZfZ7v7lJ',
                            'name': 'Undefined'
                        },
                        'family': False
                    }],
                    'upcomingEvents': {
                        '_total': 731,
                        'tmr': 411,
                        'ticketmaster': 320
                    },
                    '_links': {
                        'self': {
                            'href': '/discovery/v2/attractions/K8vZ9174wRf?locale=en-us'
                        }
                    }
                }]
            }
        }]
    },
    '_links': {
        'first': {
            'href': '/discovery/v2/events.json?page=0&size=3'
        },
        'prev': {
            'href': '/discovery/v2/events.json?page=25&size=3'
        },
        'self': {
            'href': '/discovery/v2/events.json?size=3&page=26'
        },
        'next': {
            'href': '/discovery/v2/events.json?page=27&size=3'
        },
        'last': {
            'href': '/discovery/v2/events.json?page=45863&size=3'
        }
    },
    'page': {
        'size': 3,
        'totalElements': 137590,
        'totalPages': 45864,
        'number': 26
    }
}
)

api_response_mock = MagicMock()
api_response_mock.status = 200
api_response_mock.read.return_value = api_response_value
