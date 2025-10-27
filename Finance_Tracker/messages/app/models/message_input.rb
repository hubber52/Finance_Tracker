class MessageInput < ApplicationRecord
    validates :messages, presence: true
    validates :uuid, presence: true, uniqueness: true 
end
